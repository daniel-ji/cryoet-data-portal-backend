"""
GraphQL enums

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/support/enums.py.j2 instead.
"""

import enum

import strawberry


@strawberry.enum
class tomogram_type_enum(enum.Enum):
    CANONICAL = "CANONICAL"
    UNKNOWN = "UNKNOWN"


@strawberry.enum
class annotation_file_source_enum(enum.Enum):
    dataset_author = "dataset_author"
    community = "community"
    portal_standard = "portal_standard"


@strawberry.enum
class annotation_method_type_enum(enum.Enum):
    manual = "manual"
    automated = "automated"
    hybrid = "hybrid"


@strawberry.enum
class annotation_file_shape_type_enum(enum.Enum):
    SegmentationMask = "SegmentationMask"
    OrientedPoint = "OrientedPoint"
    Point = "Point"
    InstanceSegmentation = "InstanceSegmentation"


@strawberry.enum
class annotation_method_link_type_enum(enum.Enum):
    documentation = "documentation"
    models_weights = "models_weights"
    other = "other"
    source_code = "source_code"
    website = "website"


@strawberry.enum
class deposition_types_enum(enum.Enum):
    annotation = "annotation"
    dataset = "dataset"
    tomogram = "tomogram"


@strawberry.enum
class sample_type_enum(enum.Enum):
    cell = "cell"
    tissue = "tissue"
    organism = "organism"
    organelle = "organelle"
    virus = "virus"
    in_vitro = "in_vitro"
    in_silico = "in_silico"
    other = "other"


@strawberry.enum
class tiltseries_camera_acquire_mode_enum(enum.Enum):
    counting = "counting"
    superresolution = "superresolution"
    linear = "linear"
    cds = "cds"


@strawberry.enum
class tiltseries_microscope_manufacturer_enum(enum.Enum):
    FEI = "FEI"
    TFS = "TFS"
    JEOL = "JEOL"


@strawberry.enum
class fiducial_alignment_status_enum(enum.Enum):
    FIDUCIAL = "FIDUCIAL"
    NON_FIDUCIAL = "NON_FIDUCIAL"


@strawberry.enum
class tomogram_processing_enum(enum.Enum):
    denoised = "denoised"
    filtered = "filtered"
    raw = "raw"


@strawberry.enum
class tomogram_reconstruction_method_enum(enum.Enum):
    SART = "SART"
    Fourier_Space = "Fourier_Space"
    SIRT = "SIRT"
    WBP = "WBP"
    Unknown = "Unknown"


@strawberry.enum
class alignment_type_enum(enum.Enum):
    LOCAL = "LOCAL"
    GLOBAL = "GLOBAL"
