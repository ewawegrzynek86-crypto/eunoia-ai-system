import numpy as np

# Simulated HRV data for 30 days
np.random.seed(42)
baseline_data = np.random.normal(loc=50, scale=5, size=27)

# Last 3 days – possible trend
recent_data = np.array([65, 67, 70])

# Calculate personal baseline
mean_baseline = np.mean(baseline_data)
std_baseline = np.std(baseline_data)

print(f"Baseline mean HRV: {mean_baseline:.2f}")
print(f"Baseline std HRV: {std_baseline:.2f}")

# Anomaly threshold (2 standard deviations)
threshold = mean_baseline + 2 * std_baseline

# Check if deviation persists for 3 consecutive periods
if all(value > threshold for value in recent_data):
    print("Stable deviation detected: trend identified.")
else:
    print("No stable trend detected.")
