import pandas as pd
import numpy as np
import os

# Save CSV in the same folder as script
folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(folder, "sensor_data.csv")

# Simulate 1 week of hourly readings
time_index = pd.date_range(start='2025-01-01', periods=24*7, freq='H')

# Temperature and humidity with noise
temperature = 20 + np.random.normal(0, 1, len(time_index))
humidity = 50 + np.random.normal(0, 5, len(time_index))

# Inject anomalies
temperature[50] = 35
humidity[100] = 10

# Save CSV
df = pd.DataFrame({'datetime': time_index, 'temperature': temperature, 'humidity': humidity})
df.to_csv(csv_path, index=False)
print(f"Sensor data CSV saved to {csv_path}")
