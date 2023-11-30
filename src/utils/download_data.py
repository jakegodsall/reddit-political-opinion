import zipfile
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi


def download_data(dataset_name, download_path="data", unzip = True):
    """
    Download a Kaggle dataset using the Kaggle API.

    Args:
        dataset_name (str): The name of the Kaggle dataset (e.g., 'username/dataset-name').
        download_path (str): The directory where the dataset should be downloaded. Defaults to the current directory.
        unzip (bool): Whether to unzip the downloaded dataset if it's a zip file. Defaults to True.

    Returns:
        None
    """
    root_dir = Path()
    data_dir = root_dir / download_path

    api = KaggleApi()
    api.authenticate()

    data_dir.mkdir(exist_ok=True)

    api.dataset_download_files(dataset_name, data_dir)

    print(f"Dataset '{dataset_name}' downloaded to '/{download_path}'.")

    if unzip:
        zip_file = f'{dataset_name.split("/")[-1]}.zip'
        zip_path = data_dir / zip_file
        with zipfile.ZipFile(zip_path, mode="r") as zipped:
            zipped.extractall(data_dir)
        (data_dir / zip_file).unlink()