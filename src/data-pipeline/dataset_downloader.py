"""
Project: Top-n Music Genre Classification Neural Network and CLI Application
File Name: dataset_downloader.py
Authors:
- Elvin Carmona
- Mark Jordan, github: markyjordan
- Michael Levins
Created: 2024-01-26, Updated: 2024-01-26

---

Description: This file allows a user to download open-source datasets for use in the project.

Copyright: © 2024 Elvin Carmona, Mark Jordan, Michael Levins
"""

import os
import sys
from datasets import load_dataset
try:
    import lzma     # to handle any compressed files in the dataset (.xz files)
except ImportError:
    sys.stderr.write("LZMA module not found. Please ensure your Python installation includes LZMA support.\n")


def download_dataset(dataset_name, save_path, dataset_dir_name):
    """
    Download a specified dataset and save it to a given path.

    Usage:
        python3 dataset_downloader.py

    Args:
        dataset_name (str): name of the dataset to be downloaded
        save_path (str): path to save the dataset
        dataset_dir_name (str): name of the subdirectory at save_path to save the dataset; this will be created if it does not exist

    Returns:
        None
    """
    # create the path string that will be used to save the dataset
    dataset_path = os.path.join(save_path, dataset_dir_name)

    # create the directory if it does not exist
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)

    # load and download the dataset
    dataset = load_dataset(dataset_name, cache_dir=dataset_path, trust_remote_code=True)
    dataset.save_to_disk(os.path.join(save_path, dataset_dir_name))
    print(f"{dataset_name} dataset downloaded successfully into {dataset_path}")

def download_gtzan(name="marsyas/gtzan", save_path="dataset/raw", dataset_dir_name="gtzan"):
    """
    Download the GTZAN dataset and save it to a given path.
    """
    download_dataset(name, save_path, dataset_dir_name)


if __name__ == "__main__":
    download_gtzan()