import pandas as pd
import numpy as np

# Generate date range
start_date = '2022-01-01'
end_date = '2022-12-31'
date_range = pd.date_range(start=start_date, end=end_date)

# Generate random values for the time series data
num_samples = len(date_range)
values = np.random.rand(num_samples) * 100  # Generate random values between 0 and 100

# Create DataFrame
df = pd.DataFrame({'start': date_range, 'value': values})

# Save DataFrame to Excel file
df.to_excel('data/time_series.xlsx', index=False)

print("Time series data generated and saved to 'time_series.xlsx'")
