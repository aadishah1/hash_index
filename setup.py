import os

def _create_storage_directory_if_not_exists(path="./storage"):
    if not os.path.exists(path):
        os.mkdir(path=path)


def _create_index_directory_if_not_exists(path="./index"):
    if not os.path.exists(path):
        os.mkdir(path=path)


if __name__ == "__main__":
    _create_storage_directory_if_not_exists()
    _create_index_directory_if_not_exists()
    