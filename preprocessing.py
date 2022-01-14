#import statements
import pandas as pd
import numpy as np
import pyprep

import datetime
import os

import matplotlib as plt
import mne
import mne_features.univariate as mf
import eeglib.features as ef
from sklearn.decomposition import FastICA

def clean_signals(raw_signals):
    # Load EEG data into MNE Python for preprocessing
    # Create MNE Python object
    fs = 125 # Sampling frequency of the OpenBCI recording
    ch_names = raw_signals.drop('time', axis=1).columns.values.tolist()
    info = mne.create_info(ch_names, fs, ch_types='eeg')
    raw = mne.io.RawArray(np.array(raw_signals.drop('time', axis = 1)).transpose(), info)

    # High-Pass Filter & Plot for visual inspection
    raw.copy().filter(l_freq = 1, h_freq = 62.49).plot(scalings=dict(eeg=100))

    # Load custom montage (for cEEGrids) - these are the coordinates of the electrodes on the head
    ceegrid_montage = mne.channels.read_custom_montage('ceegrid_sph.txt')
    raw = raw.copy().set_montage(ceegrid_montage)

    # Filter the data
    raw = raw.notch_filter(freqs=(25, 50)) # Notch filter to remove power line noise
    raw = raw.filter(l_freq = 1, h_freq = 62.49) # 1 Hz Highpass (detrend) & 62.5 Hz Lowpass (remove high-frequency artefacts)

    # Detect (& interpolate) bad channels
    # You can play around with this a bit if you like - it could also perform poorly in your experiment (the facial muscle artefacts are what you are interested in and should not necessarily be removed...)
    raw.info['bads'] = []
    nc = pyprep.NoisyChannels(raw, do_detrend=True, random_state=42)
    nc.find_bad_by_SNR()
    nc.find_bad_by_deviation()
    nc.find_bad_by_hfnoise()
    nc.find_bad_by_nan_flat()
    nc.find_bad_by_ransac()
    raw.info['bads'] = nc.get_bads()
    # Interpolation can be done using mne python's interpolate_bads()
    raw = raw.interpolate_bads()

    return raw

''' 
function that splits array into given "size" subarrays 
'''
def split_given_size(a, size):
    return np.split(a, np.arange(size, a.shape[1], size), axis=1)

''' 
function takes array of one closed routine and returns non-overlapping one second windows
'''
def cut_epochs_1s(array):
    #split data along axis=1
    array_list = split_given_size(array, 125)
    #drop last split if it contains less than 100 values
    if (array_list[-1].shape[1]) < 100:
        del array_list[-1]

    return array_list

'''
function calculates all features out of the NeuroIS paper.
Takes a list of arrays (which contain windows of one activity) and returns feature vector as numpy array
'''
def calculate_featuresF1(splits):

    features_one_routine = list()
    for epoch in splits:
        #forcing float
        epoch = epoch.astype(float)
        #calc sum
        summe = epoch.sum(axis=1)
        #calc max
        maxi = epoch.max(axis=1)
        #calc Hurst exponent
        hurst = mf.compute_hurst_exp(epoch)
        #calc Petrosian (katz) Frac
        petro = np.apply_along_axis(ef.PFD, axis = 1, arr = epoch)
        #calc Higuchi Fraction
        higuchi = mf.compute_higuchi_fd(epoch)
        #calc Hjorth paramers (Activity, Mobility and Complexity)
        
        acti = np.apply_along_axis(ef.hjorthActivity, axis = 1, arr = epoch)
        compl = mf.compute_hjorth_complexity(epoch)
        mobil = mf.compute_hjorth_mobility(epoch)
        #freq bandpowers
        #theta, alpha, beta = calculate_freq_bandpowers(epoch)

        feature = np.concatenate((summe, maxi, hurst, petro, higuchi, acti, compl, mobil), axis=0)
        #theta, alpha, beta
        #print(feature.shape)
        features_one_routine.append(feature)


    return features_one_routine

'''
function calculates Individual Components of signals
takes takes number of components and list of numpy arrays containing windows of activity as input
'''
def calculate_ica(components, splits):
    return_list = list()

    for epoch in splits:
        #print(epoch.shape)
        epoch_trans = epoch.transpose()
        #print(epoch.shape)
        transformer = FastICA(n_components = components, random_state = 42)

        splits_ica = transformer.fit_transform(epoch_trans)
        splits_ica = splits_ica.transpose()
        #print("Shape after ICA is applied: " + str(splits_ica.shape))
        
        concat_array = np.concatenate((epoch, splits_ica), axis = 0)
        return_list.append(concat_array)

    return return_list

'''

'''
def generate_featureSet1(data = dict):
    target_list = list()
    everything = list()

    for key, value in data.items():
        for df in value:

            transposed_df = df.transpose()
            feature_data = transposed_df.iloc[:-1:]
            array = feature_data.to_numpy()
            epochs = cut_epochs_1s(array)
            feature = calculate_featuresF1(epochs)
            for zeile in feature:
                everything.append(zeile)
                target_list.append(key)


    training_data = pd.DataFrame(everything)
    training_data['Y'] = target_list
    
    print('Feature Set 1 successfully generated..')
    print('Shape of generated Feature Set as pandas DataFrame= ' + str(training_data.shape))
    
    return training_data


'''
function generates Feature Set 2; takes a dictionary containing names of activities as keys and DataFrames which contain routines as values
'''
def generate_featureSet2(data = dict, ica_n = int):
    target_list = list()
    everything = list()

    for key, value in data.items():
        for df in value:

            transposed_df = df.transpose()
            feature_data = transposed_df.iloc[:-1:]
            array = feature_data.to_numpy()
            epochs = cut_epochs_1s(array)
            epochs = calculate_ica(components = ica_n, splits = epochs)
            feature = calculate_featuresF1(epochs)
            for zeile in feature:
                everything.append(zeile)
                target_list.append(key)


    training_data = pd.DataFrame(everything)
    training_data['Y'] = target_list
    
    print('Feature Set 2 successfully generated..')
    print('Shape of generated Feature Set as pandas DataFrame= ' + str(training_data.shape))

    return training_data




