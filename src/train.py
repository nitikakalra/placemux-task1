import random
import numpy as np

SEED = 42

random.seed(SEED)
np.random.seed(SEED)

print("Environment setup successful")
print(f"Seed value: {SEED}")