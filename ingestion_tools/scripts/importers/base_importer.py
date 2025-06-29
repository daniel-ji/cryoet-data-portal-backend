import contextlib
import os
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Optional

from common.copy import copy_by_src
from common.finders import DepositionObjectImporterFactory
from common.image import (
    VolumeInfo,
    get_volume_info,
    get_volume_metadata,
    get_voxel_size,
    make_pyramids,
)

if TYPE_CHECKING:
    from common.config import DepositionImportConfig
    from importers.annotation import BaseAnnotationSource
    from importers.dataset import DatasetImporter
    from importers.deposition import DepositionImporter
    from importers.run import RunImporter
    from importers.tomogram import TomogramImporter
    from importers.voxel_spacing import VoxelSpacingImporter
else:
    BaseAnnotationSource = "BaseAnnotationSource"
    DatasetImporter = "DatasetImporter"
    DepositionImporter = "DepositionImporter"
    DepositionImportConfig = "DepositionImportConfig"
    RunImporter = "RunImporter"
    TomogramImporter = "TomogramImporter"
    VoxelSpacingImporter = "VoxelSpacingImporter"


class BaseImporter:
    """
    Base class for importing deposition entities.

    Attributes:
        type_key (str): Specifies the type of importer.
        plural_key (str): The plural value of the type key. This will be matched against the import flag.
        cached_find_results (dict[str, BaseImporter]): Caches results of find operations.
        finder_factory (DepositionObjectImporterFactory | None): The finder factory to be employed by the importer.
        parents (dict[str, BaseImporter]): Parent importers of the current importer.
        has_metadata (bool): Indicates if the importer supports metadata import.
        dir_path (str | None): Path in the destination for the entity.
        metadata_path (str | None): Path in the destination for the metadata file.
    """

    type_key: str
    plural_key: str
    cached_find_results: dict[str, "BaseImporter"] = {}
    finder_factory: DepositionObjectImporterFactory | None = None
    parents: dict[str, "BaseImporter"]
    has_metadata: bool = False
    dir_path: str | None = None
    metadata_path: str | None = None

    def __init__(
        self,
        config: "DepositionImportConfig",
        metadata: dict[str, Any],
        name: Optional[str] = None,
        path: Optional[str] = None,
        allow_imports: bool = True,
        parents: Optional[dict[str, "BaseImporter"]] = None,
        *args,
        **kwargs,
    ):
        self.config = config
        self.metadata = metadata
        self.name = name
        self.path = path
        self.allow_imports = allow_imports

        if parents is None:
            parents = {}
        self.parents = parents

    def parent_getter(self, type_key: str) -> "BaseImporter":
        if self.type_key == type_key:
            return self
        return self.parents[type_key]

    def get_glob_vars(self) -> dict[str, Any]:
        """
        Retrieves values that are supported for globbing a file from the current importer and all its parents. Some of the
        supported values include path, name, id (if the importer supports it), etc.

        Returns:
           dict[str, Any]: A dictionary containing glob variables.
        """
        glob_vars = {}
        glob_vars[f"{self.type_key}_path"] = self.path
        glob_vars[f"{self.type_key}_name"] = self.name
        if hasattr(self, "identifier") and self.identifier:
            glob_vars[f"{self.type_key}_id"] = self.identifier
        with contextlib.suppress(ValueError, TypeError):
            glob_vars[f"int_{self.type_key}_name"] = int(self.name)

        # TODO FIXME this should probably be moved to the RunImporter
        if self.type_key == "run":
            run_name = self.name
            glob_vars.update(self.config.get_run_data_map(run_name))

            # TODO: we want to remove these in favor of the singular tsv file!
            glob_vars["mapped_tomo_name"] = self.config.run_to_tomo_map.get(run_name)
            glob_vars["mapped_frame_name"] = self.config.run_to_frame_map.get(run_name)
            glob_vars["mapped_ts_name"] = self.config.run_to_ts_map.get(run_name)

        if self.parents:
            for parent in self.parents.values():
                glob_vars.update(parent.get_glob_vars())
        return glob_vars

    def get_deposition(self) -> DepositionImporter:
        return self.parent_getter("deposition")

    def get_dataset(self) -> DatasetImporter:
        return self.parent_getter("dataset")

    def get_run(self) -> RunImporter:
        return self.parent_getter("run")

    def get_tomogram(self) -> TomogramImporter:
        return self.parent_getter("tomogram")

    def get_voxel_spacing(self) -> VoxelSpacingImporter:
        return self.parent_getter("voxel_spacing")

    def get_annotation(self) -> BaseAnnotationSource:
        return self.parent_getter("annotation")

    def get_output_path(self) -> str:
        """
        Retrieves the output path for the current importer.

        This method constructs the output path by combining the base output path
        from the configuration with self.dir_path string formatted with the required values.
        Returns:
            str: The constructed output path.
        """
        return self.config.get_output_path(self)

    def get_base_metadata(self) -> dict[str, Any]:
        """
        Retrieves a deep copy od the metadata for the importer specified in the config. For tiltseries and tomograms
        importers the metadata is expanded to support any string replacements.
        """
        return self.config.get_expanded_metadata(self)

    def get_metadata_path(self) -> str:
        """
        Retrieves the metadata path for the current importer.

        Returns:
           str: The constructed metadata path.
        """
        return self.config.get_metadata_path(self)

    def is_import_allowed(self):
        return self.allow_imports

    @classmethod
    def finder(cls, config: DepositionImportConfig, **parents: dict[str, "BaseImporter"]) -> Iterator["BaseImporter"]:
        """
        Finds the importer entities based on the configuration source specified. If no items are found, but a default
        entry exists, then the default entry is returned.
        Returns:
            list[BaseImporter]: A list of importer entities.
        """
        finder_configs = config.get_object_configs(cls.type_key)
        item_found = False
        for item in cls._finder_execution(finder_configs, config, **parents):
            item_found = True
            yield item
        if not item_found and (default_config := cls.get_default_config()):
            for item in cls._finder_execution(default_config, config, **parents):
                yield item

    @classmethod
    def get_default_config(cls) -> list[dict] | None:
        """
        Returns a default configuration for the importer. This value is set as default configuration for the importer
        if no entry exists for it in the configuration or if the source finders aren't able to find any matches.
        Override this method in subclasses where an entity is always required even if there is no config provided or an
        invalid config source is provided.

        Returns:
        list[dict] | None: The default configuration for the importer. If no entry exists, returns None.
        """
        return None

    @classmethod
    def get_name_and_path(cls, metadata: dict, name: str, path: str, results: dict[str, str]) -> [str, str, dict]:
        """
        Returns the name, path and a dictionary of name and paths for the importer. This method is used to override the
        name and path for the importer when the destination metadata is provided.
        :param metadata: the metadata associated to the relevant importer entity
        :param name: the name identified for the importer entity
        :param path: the path for the importer entity
        :param results: a dict of the filename and path for the importer entity
        :return:
        """
        NotImplemented("Subclasses must implement this method")

    @classmethod
    def _finder_execution(
        cls,
        finder_configs: list[dict],
        config: DepositionImportConfig,
        **parents: dict[str, "BaseImporter"],
    ) -> list["BaseImporter"]:
        """
        Executes the finder action for the importer. The configuration is used for determining the type of finder to be
        used.
        """
        for finder in finder_configs:
            metadata = finder.get("metadata", {})
            sources = finder.get("sources", [])
            for source in sources:
                source_finder_factory = cls.finder_factory(source, cls)
                for item in source_finder_factory.find(config, metadata, **parents):
                    yield item

    def __repr__(self) -> str:
        if self.name:
            return f"{self.type_key}: <{self.name}>"
        return super().__repr__()


class VolumeImporter(BaseImporter):
    """
    A class for importing volume data.

    This class extends the BaseImporter to handle the import of volume data, including scaling and metadata handling.

    Attributes:
        volume_filename (str): The filename of the volume to be imported.
        identifier (Any): An identifier for the volume importer.
    """

    def __init__(
        self,
        path: str,
        *args: list[Any],
        **kwargs: dict[str, Any],
    ):
        super().__init__(*args, **kwargs)
        self.volume_filename = path
        self.identifier = None

    def get_voxel_size(self) -> float:
        """
        Retrieves the voxel size of the source volume.
        Returns:
            float: voxel size of the source.
        """
        return get_voxel_size(self.config.fs, self.volume_filename)

    def get_output_volume_info(self) -> VolumeInfo:
        output_prefix = self.get_output_path()
        return get_volume_info(self.config.fs, f"{output_prefix}.mrc")

    def scale_mrcfile(
        self,
        scale_z_axis: bool = True,
        write_zarr: bool = True,
        write_mrc: bool = True,
        voxel_spacing: float | None = None,
    ) -> dict[str, Any]:
        """
        Scales the MRC file into a pyramid volume and optionally writes it to MRC and Zarr formats.
        The mrc file written is the most detailed level of the pyramid.
        The zarr file written is the full pyramid.
        Args:
            scale_z_axis (bool): Whether to scale the z-axis.
            write_zarr (bool): Whether to write the zarr file.
            write_mrc (bool): Whether to write the mrc file.
            voxel_spacing (float): The voxel spacing of the volume.
        """
        output_prefix = self.get_output_path()
        return make_pyramids(
            self.config.fs,
            output_prefix,
            self.volume_filename,
            scale_z_axis=scale_z_axis,
            write_mrc=write_mrc,
            write_zarr=write_zarr,
            header_mapper=self.mrc_header_mapper,
            voxel_spacing=voxel_spacing,
        )

    def get_output_path(self) -> str:
        output_dir = super().get_output_path()
        return os.path.join(output_dir, self.get_run().name)

    def load_extra_metadata(self) -> dict[str, Any]:
        run: RunImporter = self.get_run()
        output_prefix = self.get_output_path()
        metadata = get_volume_metadata(self.config, output_prefix)
        metadata["run_name"] = run.name
        return metadata

    def mrc_header_mapper(self, header):
        pass


class BaseFileImporter(BaseImporter):
    """
    This class extends the BaseImporter to handle the import of files. This is suited for case where no transformations
    are required, and source files can be copied to the destination.
    """

    def get_destination_path(self) -> str:
        return os.path.join(self.get_output_path(), os.path.basename(self.path))

    def import_item(self) -> None:
        if not self.is_import_allowed():
            print(f"Skipping import of {self.name}")
            return
        self.config.fs.copy(self.path, self.get_destination_path())


class BaseKeyPhotoImporter(BaseImporter):
    """
    This class extends the BaseImporter to handle the import of key photos. This importer supports copying of images from
    a source, and generating the image based on its parent importer.
    """

    image_keys = ["snapshot", "thumbnail"]

    def import_item(self) -> None:
        if not self.is_import_allowed():
            print(f"Skipping import of {self.name}")
            return
        dest_path = self.config.get_output_path(self)
        self.save_image(self.name, dest_path)

    def get_image_src_path(self) -> str | None:
        raise NotImplementedError("Subclasses must implement this method")

    def save_image(self, key: str, path: str) -> None:
        image_src = self.get_image_src_path()
        if not image_src:
            return None
        _, extension = os.path.splitext(image_src)
        dest_path = os.path.join(path, key) + extension
        copy_by_src(image_src, dest_path, self.config.fs)

    def get_metadata(self) -> dict[str, str]:
        """
        Retrieves the path for the current importer's pre-defined keys.
        """
        path = self.config.get_output_path(self)
        image_files = self.config.fs.glob(f"{path}/*")
        return {key: self.get_image_file(image_files, f"{path}/{key}") for key in self.image_keys}

    def get_image_file(self, key_photo_files: list[str], prefix: str) -> str | None:
        image_path = next(filter(lambda file: file.startswith(prefix), key_photo_files), None)
        if image_path:
            return os.path.relpath(image_path, self.config.output_prefix)
        return None
