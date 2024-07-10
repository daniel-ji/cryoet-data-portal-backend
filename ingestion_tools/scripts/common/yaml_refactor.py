import os
import re

DATASET_CONFIGS_DIR = "../dataset_configs/"
EXCLUDE_LIST = ["template.yaml", "dataset_config_merged.yaml"]
EXCLUDE_KEYWORDS = "draft"
YAML_EXTENSIONS = (".yaml", ".yml")


def get_files_to_refactor(
    include_glob: str = None,
    exclude_keywords: str = EXCLUDE_KEYWORDS,
    dataset_configs_dir: str = DATASET_CONFIGS_DIR,
) -> list:
    """
    Returns a list of files to validate based on the include glob and exclude keywords.
    """
    exclude_keywords_list = exclude_keywords.split(",")
    if exclude_keywords_list[0] != "":
        print(f"[INFO]: Excluding files that contain any of the following keywords: {exclude_keywords_list}")
    else:
        exclude_keywords_list = []

    # Get all YAML files in the dataset_configs directory
    all_files = []
    for root, _, files in os.walk(dataset_configs_dir):
        for file in files:
            if file.endswith(YAML_EXTENSIONS):
                all_files.append(os.path.join(root, file))

    # Filter files based on the exclude list
    files_to_validate = []
    for file in all_files:
        filename = os.path.basename(file)
        if filename in EXCLUDE_LIST:
            continue
        if any(keyword in filename for keyword in exclude_keywords_list):
            print(f"[INFO]: Excluding {file} because it contains an exclude keyword")
            continue
        files_to_validate.append(file)

    # Filter files based on the include glob
    if include_glob:
        print(f"[INFO]: Filtering files based on include glob: {include_glob}")
        files_to_validate = [file for file in files_to_validate if re.search(include_glob, file)]

    return files_to_validate
