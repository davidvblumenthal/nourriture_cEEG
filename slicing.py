#import statements
import pandas as pd
import numpy as np
import datetime
import os

import matplotlib as plt
import itertools
import mne

def import_experiment_data():
    path = 'experiment/data/'
    
    dfs = []
    
    csv_files = [csv for csv in os.listdir(path) if csv.endswith('.csv')]
    
    for file in csv_files:
        df = pd.read_csv(path + file)
        dfs.append(df)
    df = pd.concat(dfs)
    return df

def import_sensor_data(): 
    sensor_data1 = pd.read_csv('eeg_data/David.txt',header=[0],sep=',')
    sensor_data2 = pd.read_csv('eeg_data/Lukas.txt',header=[0],sep=',')
    sensor_data = sensor_data1.append(sensor_data2, ignore_index=True)
    sensor_data[" Timestamp"].replace(' 0.0', np.nan, inplace=True)
    sensor_data = sensor_data[sensor_data[' Timestamp'].notna()]
    dates = []
    for timestamps in sensor_data[" Timestamp (Formatted)"].values:
        dates.append(datetime.datetime.strptime(timestamps[1:].replace(".",":"),'%Y-%m-%d %H:%M:%S:%f' ))
    sensor_data[" Timestamp (Formatted)"] = dates
    return sensor_data

def convert_timestamps(sensor_data):
    dates = []
    for timestamps in sensor_data[" Timestamp (Formatted)"].values:
        dates.append(datetime.datetime.strptime(timestamps[1:].replace(".",":"),'%Y-%m-%d %H:%M:%S:%f' ))
    sensor_data[" Timestamp (Formatted)"] = dates
    return sensor_data

def get_routine_times(df):
    columns = ['TIMESTAMP_Speaking_Start', 'TIMESTAMP_Speaking_End', 'TIMESTAMP_Yawning_Start', 'TIMESTAMP_Yawning_End', 
           'TIMESTAMP_Resting_Start', 'TIMESTAMP_Resting_End', 'TIMESTAMP_Resting_Eyes_Closed_Start', 'TIMESTAMP_Resting_Eyes_Closed_End', 
           'TIMESTAMP_Eating_NSF_Start', 'TIMESTAMP_Eating_NSF_End', 'TIMESTAMP_Eating_Nuts_Start', 'TIMESTAMP_Eating_Nuts_End', 
           'TIMESTAMP_Eating_Bread_Start', 'TIMESTAMP_Eating_Bread_End'
          ]
    data = df[columns]
    liste = []

    for column_name in columns:
        column = data.dropna(subset=[column_name])
        values = column[column_name].values.tolist()
        liste.append(values)
    data = {}
    for column, value in zip(columns, liste):
        data[column] =  value
    speaking = pd.DataFrame(data = dict(itertools.islice(data.items(), 2)))
    yawning = pd.DataFrame(data = dict(itertools.islice(data.items(), 2, 4)))
    resting_open = pd.DataFrame(data = dict(itertools.islice(data.items(), 4, 6)))
    resting_closed = pd.DataFrame(data = dict(itertools.islice(data.items(), 6, 8)))
    soup = pd.DataFrame(data = dict(itertools.islice(data.items(), 8, 10)))
    nuts = pd.DataFrame(data = dict(itertools.islice(data.items(), 10, 12)))
    sandwich = pd.DataFrame(dict(itertools.islice(data.items(), 12, 14)))
    routines = {"speaking":speaking,"yawning": yawning,"resting_open": resting_open,"resting_closed": resting_closed, "soup":soup, "nuts": nuts,"sandwich": sandwich}
    for activities in routines.values(): 
        TF_TS_Start = []
        TF_TS_End = []
        for start, end in activities.itertuples(index=False):
            #TF = Transformed from UNIX into Timestamp
            startTS = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S:%f')
            endTS = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S:%f')
            #just take last 3 digits of 
            TF_TS_Start.append(startTS[:-3])
            TF_TS_End.append(endTS[:-3])
        activities["TF_TS_Start"]=TF_TS_Start
        activities["TF_TS_End"]=TF_TS_End
    return routines 

def slice_data(routines, sensor_data): 
    routines_data_dict = {}
    for key, values in routines.items():
        list_of_all_routines = []
        for i in values.index:
            start = datetime.datetime.strptime(values.TF_TS_Start[i], '%Y-%m-%d %H:%M:%S:%f')
            end = datetime.datetime.strptime(values.TF_TS_End[i], '%Y-%m-%d %H:%M:%S:%f')
            df = sensor_data[(sensor_data[' Timestamp (Formatted)'] > start) & (sensor_data[' Timestamp (Formatted)'] <= end)]
            df["target"]=key
            list_of_all_routines.append(df)
            df_name = key
            routines_data_dict[df_name] = list_of_all_routines
    factorization = {"speaking":0,"yawning": 1,"resting_open": 2,"resting_closed": 3, "soup":4, "nuts": 5,"sandwich": 6}
    factorization.items()
    for key, values in factorization.items():
        for i in range(len(routines_data_dict[key])):
            routines_data_dict[key][i]["target"].replace(key,str(factorization[key]),inplace=True)
            routines_data_dict[key][i].drop(" Timestamp (Formatted)", inplace=True, axis=1)
    return routines_data_dict

