import os
import time

def create_new_db_file(file_name, storage_path="./storage"):
    if not os.path.exists(os.path.join(storage_path, file_name)):
        open(os.path.join(storage_path, file_name), 'a').close()


def _determine_new_file_name(storage_path="./storage"):
    if os.path.exists(storage_path):
        return f"db_file_{int(time.time() // 1)}"
    

if __name__ == "__main__":
    create_new_db_file(_determine_new_file_name())