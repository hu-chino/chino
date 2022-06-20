import numpy as np


def read_csv(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    lines = [l.strip().split(",") for l in lines]
    data = np.array(lines, dtype=np.float)
    return data