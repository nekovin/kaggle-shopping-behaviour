import shutil
from pathlib import Path

import kagglehub


def pull_data():
    cache_path = kagglehub.dataset_download(
        "ranaghulamnabi/shopping-behavior-and-preferences-study"
    )

    dest = Path("data/raw")
    dest.mkdir(parents=True, exist_ok=True)

    for f in Path(cache_path).iterdir():
        target = dest / f.name
        if f.is_dir():
            shutil.copytree(f, target, dirs_exist_ok=True)
        else:
            shutil.copy(f, target)

    print(f"Downloaded to: {dest.resolve()}")