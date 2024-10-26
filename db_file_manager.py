import os
import time
import glob

def create_new_db_file(file_name, storage_path="./storage"):
    if not os.path.exists(os.path.join(storage_path, file_name)):
        open(os.path.join(storage_path, file_name), 'a').close()


def _determine_new_file_name(storage_path="./storage"):
    if os.path.exists(storage_path):
        return f"db_file_{int(time.time() // 1)}"
    

def get_timestamp_from_file_name(filename):
    try:
        return int(filename.split('_')[-1])
    except (ValueError, IndexError):
        return 0


def get_files_sorted_in_descending_order(path):
    if (os.path.exists(path)):
        files = glob.glob("./storage/*")
        
        sorted_files = sorted(files, key=lambda f: f.split("_")[-1], reverse=True)
        
        return sorted_files


if __name__ == "__main__":
    create_new_db_file(_determine_new_file_name())