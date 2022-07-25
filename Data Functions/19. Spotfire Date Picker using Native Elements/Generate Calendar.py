import pandas as pd
import numpy as np

#Credits : https://stackoverflow.com/a/47150710
import datetime as dt

def create_date_table(start='2000-01-01', end='2050-12-31'):
    start_ts = pd.to_datetime(start).date()

    end_ts = pd.to_datetime(end).date()

    # record timetsamp is empty for now
    dates =  pd.DataFrame(columns=['Record_timestamp'],
        index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'Date'

    days_names = {
        i: name
        for i, name
        in enumerate(['Monday', 'Tuesday', 'Wednesday',
                      'Thursday', 'Friday', 'Saturday', 
                      'Sunday'])
    }

    dates['Day'] = dates.index.dayofweek.map(days_names.get)
    dates['Week'] = dates.index.week
    dates['Month'] = dates.index.month
    dates['Quarter'] = dates.index.quarter
    dates['Year_half'] = dates.index.month.map(lambda mth: 1 if mth <7 else 2)
    dates['Year'] = dates.index.year
    dates.reset_index(inplace=True)
    dates.index.name = 'date_id'
    return dates

df =create_date_table(start='2021-01-01', end='2023-12-31')
df.pop('Record_timestamp')