#import statements
import pandas as pd
import numpy as np
import pyprep

import datetime
import os

import matplotlib as plt
import mne

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