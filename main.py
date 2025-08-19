import matplotlib.pyplot as plt

# Data
groups = ["Children", "Adults", "Elderly"]
total = [50, 200, 60]
survived = [40, 80, 20]

# Plot
plt.bar(groups, total, color="darkred", label="Total")
plt.bar(groups, survived, color="blue", label="Survived")

plt.xlabel("Groups")
plt.ylabel("People")
plt.title("Titanic - Total vs Survived")
plt.legend()
plt.show()