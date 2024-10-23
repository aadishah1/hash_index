import argparse
import glob
import os

parser = argparse.ArgumentParser(
    prog='HashIndex',
    description='Store key value pairs',
    epilog='Reference: Designing Data Intensive Applications'
)

parser.add_argument('-k', '--key', required=True, help="The key that has to be added")
parser.add_argument('-v', '--value', required=True, help="A value corresponding to the key added")

args = parser.parse_args()
print(f"Arguments provided -> key: {args.key} and value: {args.value}")

list_of_files = glob.glob('./storage/*')
latest_file = ""
if (len(list_of_files) > 0):
    latest_file = max(list_of_files, key=os.path.getctime)

if os.path.exists(latest_file):
    with open(latest_file, "a") as latest_db_file:
        latest_db_file.write(f"{args.key},{args.value}\n")