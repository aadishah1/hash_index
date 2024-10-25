import argparse
import glob
import os

def set_key_value(key, value):
    list_of_files = glob.glob('./storage/*')
    latest_file = ""
    if (len(list_of_files) > 0):
        latest_file = max(list_of_files, key=os.path.getctime)
    print(f"FOUND latest file: {latest_file}")

    if os.path.exists(latest_file):
        print(f"Opening latest_file in append mode and writing data... {key} {value}")
        with open(latest_file, "a") as latest_db_file:
            latest_db_file.write(f"{key},{value}\n")


def get_key(key):
    pass
