import os
from pathlib import Path

data_dir = Path(os.getenv('PATH_DIR')) / 'data'
german_credit = data_dir / 'german_credit_data.csv'