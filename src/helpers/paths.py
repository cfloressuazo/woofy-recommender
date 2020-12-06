import os
from pathlib import Path

DATA_RAW_DIR = 'data/raw'
DATA_RAW_FILE = 'tiendapet.jl'

project_dir = Path().cwd().parent
data_raw_path = project_dir.joinpath(DATA_RAW_DIR)
data_raw_file_path = data_raw_path.joinpath(DATA_RAW_FILE)