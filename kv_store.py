import os
import subprocess
from db_file_manager import get_files_sorted_in_descending_order, create_new_db_file, determine_new_file_name
from config_reader import Config

config = Config()

def set_key_value(key, value):
    latest_file = ""
    files_list = get_files_sorted_in_descending_order("./storage")
    print(f"Files list: {files_list}")
    if (len(files_list) > 0):
        latest_file = files_list[0]

    file_line_count = int(subprocess.check_output(['wc', '-l', latest_file]).split()[0])
    if file_line_count >= config.get_key_from_config("db_file_threshold"):
        create_new_db_file(determine_new_file_name())
        latest_file = get_files_sorted_in_descending_order("./storage")[0] # TODO: Improve logic to make code less redundant

    print(f"FOUND latest file: {latest_file}")

    if os.path.exists(latest_file):
        print(f"Opening latest_file in append mode and writing data... {key} {value}")
        with open(latest_file, "a") as latest_db_file:
            latest_db_file.write(f"{key},{value}\n")


def get_key(key):
    list_of_files_sorted_by_latest = get_files_sorted_in_descending_order("./storage")
    print(f"List of files sorted : {list_of_files_sorted_by_latest}")

    for file in list_of_files_sorted_by_latest:
        print(f"Finding in file {file}...")
        try:
            grep_process = subprocess.Popen(
                ["grep", key.strip(), file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            sed_process = subprocess.Popen(
                ["sed", "-e", f"s/^{key},//"],
                stdin=grep_process.stdout,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            tail_process = subprocess.Popen(
                ["tail", "-n", "1"],
                stdin=sed_process.stdout,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            grep_process.stdout.close()
            sed_process.stdout.close()
        
            output, error = tail_process.communicate()

            grep_process.wait()
            sed_process.wait()
            tail_process.wait()

            for proc, name in [(grep_process, 'grep'), (sed_process, 'sed'), (tail_process, 'tail')]:
                if proc.returncode not in [0, 1, None]:
                    raise subprocess.CalledProcessError(
                        proc.returncode,
                        name,
                        error
                    )

            if grep_process.returncode == 0:
                return output.strip()

        except subprocess.CalledProcessError as e:
            if e.returncode == 1 and e.cmd == "grep":
                return "-None-"

            raise Exception(f"Command failed with error: {e.stderr}")

    return "-None-"
 
if __name__ == "__main__":
    key = "key2"
    val = get_key(key)
    print(f"{key}: {val}")