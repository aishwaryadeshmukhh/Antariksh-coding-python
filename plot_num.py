import matplotlib.pyplot as plt
import numpy as np

# sample data
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
impressions = np.array([2000, 2200, 2500, 2800, 3000, 3200])
sales = np.array([100, 120, 150, 180, 200, 220])

# plotting
plt.figure(figsize=(10, 4))

plt.plot(months, impressions, marker='o', linestyle='-', color='g', label='Social Media Impressions')

plt.plot(months, sales, marker='s', linestyle='--', color='r', label='Sales')

plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Influence of Social Media on Sales')

#plt.grid(True)

plt.legend()

plt.tight_layout()
plt.show()