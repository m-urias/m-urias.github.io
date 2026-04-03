import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred
fred = Fred(api_key='9c70445138df124be4928605b7e08bd4')

# List of industries you want to track
industries = {
    'JTSJOL': 'Total Nonfarm',
    'JTS2300JOL': 'Construction',
    'JTS3000JOL': 'Manufacturing',
    'JTS4000JOL': 'Trade, Trans, Utilities',
    'JTS5100JOL': 'Information',
    'JTS5200JOL': 'Financial Activities',
    'JTS5400JOL': 'Prof and Business Services',
    'JTS6000JOL': 'Edu and Health Services',
    'JTS7000JOL': 'Leisure and Hospitality'
}

data_list = []
for series_id, name in industries.items():
    series_data = fred.get_series(series_id)
    series_data.name = name
    data_list.append(series_data)

# Combine into one DataFrame
df = pd.concat(data_list, axis=1)
print(df.tail())
