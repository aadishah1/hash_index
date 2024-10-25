#!/bin/bash

python3 setup.py

# If storage directory is empty initially, create first DB file
if [ -z "$( ls -A './storage' )" ]; then
    python3 db_file_manager.py
fi