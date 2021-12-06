import os

INPUT_DATASET = "Datasets/Original"

BASE_PATH = "Datasets/IDC"

TRAIN_PATH = os.path.sep.join([BASE_PATH , "training"])

TEST_PATH = os.path.sep.join([BASE_PATH , "testing"])

VAL_PATH = os.path.sep.join([BASE_PATH , "validation"])


TRAIN_SPLIT = 0.8

VAL_SPLIT = 0.1



