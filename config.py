import os 
import random
from pathlib import Path, path 

import numpy as np
from box import ConfigBox
from ruamel.yaml import YAML


class Config:
    class Path:

        APP_HOME = Path(os.getenv("APP_HOME",Path(__file__).parent.parent))
        ARTIFACTS_DIR = APP_HOME / "artifacts"
        DATA_DIR = ARTIFACTS_DIR / "data"
        FEATURE_DIR = ARTIFACTS_DIR / "features"
        MODELS_DIR = ARTIFACTS_DIR / "models"
        EXPERIMENTS_DIR = APP_HOME / "experiments"


def load_config(file_path:Path = Config.Path.APP_HOME / "params.yaml") -> Configbox:
    yaml = YAML(type="safe")
    return ConfigBox(yaml.load(file_path.open(encoding="utf-8")))


def seed_everything(seed:int=load_config().random_seed):
    random.seed(seed)
    np.random.seed(seed)

