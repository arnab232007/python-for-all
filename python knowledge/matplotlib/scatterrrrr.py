import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

data = {
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
plt.scatter(df["x"], df["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot")
plt.show()
