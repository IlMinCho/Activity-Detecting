# -*- coding: utf-8 -*-
"""
This file is used for extracting features over windows of tri-axial accelerometer 
data. We recommend using helper functions like _compute_mean_features(window) to 
extract individual features.

As a side note, the underscore at the beginning of a function is a Python 
convention indicating that the function has private access (although in reality 
it is still publicly accessible).

"""

import numpy as np
from scipy.signal import find_peaks


def _compute_mean_features(window):
    """
    Computes the mean x, y and z acceleration over the given window. 
    """
    # axis 0 not necessary
    return np.mean(window, axis=0)

# TODO: define functions to compute more features

def _compute_magnitude_array(window):
    return np.sqrt(np.sum(window**2, axis=1))

def _compute_var_features(window):
    return np.var(window)

def _compute_med_features(window):
    return np.median(window)

def _compute_fft_features(window):
    fft_signal = np.fft.rfft(window)
    fft_signal = fft_signal.astype(float)
    return fft_signal[0]

from scipy.stats import entropy
def _compute_ent_features(window, num_bins):
    hist, bins = np.histogram(window, bins='auto')
    entropyval = entropy(hist, base=2)
    return entropyval

# num peaks, maybe change back to mpd
def _compute_mpd_features(window, h):
    peaks, _ = find_peaks(window, height=h)
    distances = np.diff(peaks)
    return len(peaks)

def extract_features(window):
    """
    Here is where you will extract your features from the data over 
    the given window. We have given you an example of computing 
    the mean and appending it to the feature vector.
    
    """

    """
    Statistical
    These include the mean, variance and the rate of zero- or mean-crossings. The
    minimum and maximum may be useful, as might the median
    
    FFT features
    use rfft() to get Discrete Fourier Transform
    
    Entropy
    Integrating acceleration
    
    Peak Features:
    Sometimes the count or location of peaks or troughs in the accelerometer signal can be
    an indicator of the type of activity being performed. This is basically what you did in
    assignment A1 to detect steps. Use the peak count over each window as a feature. Or
    try something like the average duration between peaks in a window.
    """

    
    x = []
    feature_names = []
    win = np.array(window)
    x.append(_compute_mean_features(win[:,0]))
    feature_names.append("x_mean")

    x.append(_compute_mean_features(win[:,1]))
    feature_names.append("y_mean")

    x.append(_compute_mean_features(win[:,2]))
    feature_names.append("z_mean")

    # TODO: call functions to compute other features. Append the features to x and the names of these features to feature_names

    x.append(_compute_mean_features(_compute_magnitude_array(win)))
    feature_names.append("mag_mean")

    # # Variance
    # x.append(_compute_var_features(win[:,0]))
    # feature_names.append("x_var")
    # x.append(_compute_var_features(win[:,1]))
    # feature_names.append("y_var")
    # x.append(_compute_var_features(win[:,2]))
    # feature_names.append("z_var")
    # x.append(_compute_var_features(_compute_magnitude_array(win)))
    # feature_names.append("mag_var")

    # # Median
    # x.append(_compute_med_features(win[:,0]))
    # feature_names.append("x_med")
    # x.append(_compute_med_features(win[:,1]))
    # feature_names.append("y_med")
    # x.append(_compute_med_features(win[:,2]))
    # feature_names.append("z_med")
    # x.append(_compute_med_features(_compute_magnitude_array(win)))
    # feature_names.append("mag_med")

    # FFT
    x.append(_compute_fft_features(win[:,0]))
    feature_names.append("x_med")
    x.append(_compute_fft_features(win[:,1]))
    feature_names.append("y_med")
    x.append(_compute_fft_features(win[:,2]))
    feature_names.append("z_med")
    x.append(_compute_med_features(_compute_magnitude_array(win)))
    feature_names.append("mag_med")

    # Entropy NAN
    num_bins = 10
    x.append(_compute_ent_features(win[:,0], num_bins))
    feature_names.append("x_ent")
    x.append(_compute_ent_features(win[:,1], num_bins))
    feature_names.append("y_ent")
    x.append(_compute_ent_features(win[:,2], num_bins))
    feature_names.append("z_ent")
    x.append(_compute_ent_features(_compute_magnitude_array(win), num_bins))
    feature_names.append("mag_ent")

    # Num peaks
    height = 0
    x.append(_compute_mpd_features(win[:,0], height))
    feature_names.append("x_mpd")
    x.append(_compute_mpd_features(win[:,1], height))
    feature_names.append("y_mpd")
    x.append(_compute_mpd_features(win[:,2], height))
    feature_names.append("z_mpd")
    x.append(_compute_mpd_features(_compute_magnitude_array(win), height))
    feature_names.append("mag_mpd")

    feature_vector = list(x)
    return feature_names, feature_vector