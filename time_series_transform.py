import pandas as pd

# Load the Excel file
df = pd.read_excel('data/time_series.xlsx')

# Create a DataFrame for each bot's working periods
def transform_data(df):
    df['start'] = pd.to_datetime(df['start'])
    df = df.sort_values(by=['start'])

    result = []
    current_bot = 1
    for _, row in df.iterrows():
        result.append([current_bot, row['start'], row['value']])
        current_bot += 1
    
    return pd.DataFrame(result, columns=['bot', 'start', 'activity'])

transformed_df = transform_data(df)
transformed_df.to_csv('data/transformed_time_series.csv', index=False)
