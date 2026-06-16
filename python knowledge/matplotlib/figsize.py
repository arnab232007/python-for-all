import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# STEP 1: Choose the canvas size FIRST
plt.figure(figsize=(8, 5))

# STEP 2: Now do your plotting
plt.plot(x, y, label="Sales")
plt.legend()
plt.title("Widescreen Sales Chart")

plt.show()