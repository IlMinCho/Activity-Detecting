# -*- coding: utf-8 -*-
"""
This is the script used to train an activity recognition 
classifier on accelerometer data.

"""

import os
import sys
import numpy as np
import sklearn
from sklearn.tree import export_graphviz
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from features import extract_features
from sklearn.metrics import confusion_matrix
from util import slidingWindow, reorient, reset_vars
import pickle

import labels


# %%---------------------------------------------------------------------------
#
#		                 Load Data From Disk
#
# -----------------------------------------------------------------------------

print("Loading data...")
sys.stdout.flush()
data_file = 'data/all_labeled_data.csv'
data = np.genfromtxt(data_file, delimiter=',')
print("Loaded {} raw labelled activity data samples.".format(len(data)))
sys.stdout.flush()

# %%---------------------------------------------------------------------------
#
#		                    Pre-processing
#
# -----------------------------------------------------------------------------

print("Reorienting accelerometer data...")
sys.stdout.flush()
reset_vars()
reoriented = np.asarray([reorient(data[i,2], data[i,3], data[i,4]) for i in range(len(data))])
reoriented_data_with_timestamps = np.append(data[:,0:2],reoriented,axis=1)
data = np.append(reoriented_data_with_timestamps, data[:,-1:], axis=1)

data = np.nan_to_num(data)

# %%---------------------------------------------------------------------------
#
#		                Extract Features & Labels
#
# -----------------------------------------------------------------------------

window_size = 20
step_size = 20

# sampling rate should be about 100 Hz (sensor logger app); you can take a brief window to confirm this
n_samples = 1000
time_elapsed_seconds = (data[n_samples,1] - data[0,1])
sampling_rate = n_samples / time_elapsed_seconds

print("Sampling Rate: " + str(sampling_rate))

# TODO: list the class labels that you collected data for in the order of label_index (defined in labels.py)
class_names = labels.activity_labels

print("Extracting features and labels for window size {} and step size {}...".format(window_size, step_size))
sys.stdout.flush()

X = []
Y = []
feature_names = []
for i,window_with_timestamp_and_label in slidingWindow(data, window_size, step_size):
    window = window_with_timestamp_and_label[:,2:-1]
    # print("window = ")
    # print(window)
    feature_names, x = extract_features(window)
    X.append(x)
    Y.append(window_with_timestamp_and_label[10, -1])
    
X = np.asarray(X)
Y = np.asarray(Y)
n_features = len(X)
    
print("Finished feature extraction over {} windows".format(len(X)))
print("Unique labels found: {}".format(set(Y)))
print("\n")
sys.stdout.flush()

# %%---------------------------------------------------------------------------
#
#		                Train & Evaluate Classifier
#
# -----------------------------------------------------------------------------


# TODO: split data into train and test datasets using 10-fold cross validation

"""
TODO: iterating over each fold, fit a decision tree classifier on the training set.
Then predict the class labels for the test set and compute the confusion matrix
using predicted labels and ground truth values. Print the accuracy, precision and recall
for each fold.
"""

cv = model_selection.KFold(n_splits=10, random_state=None, shuffle=True)


# Accuracy, precision, recall
from sklearn.metrics import accuracy_score, precision_score, recall_score
acc_scores = []
prec_scores = []
rec_scores = []

# X_test is the feature matrix for test set, Y_test is the true class label for test set
for train_index, test_index in cv.split(X):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    # predict class labels for the test set
    tree = DecisionTreeClassifier(criterion="entropy", max_depth=3)
    tree.fit(X_train, Y_train)
    Y_pred = tree.predict(X_test)
    
    # Confusion matrix for each fold
    conf = confusion_matrix(Y_test, Y_pred)

    # Append values for accuracy, precision, and recall
    # LOOK INTO WEIGHTED
    acc_scores.append(accuracy_score(Y_test, Y_pred))
    prec_scores.append(precision_score(Y_test, Y_pred, average='weighted'))
    rec_scores.append(recall_score(Y_test, Y_pred, average='weighted'))

# Compute averages
avg_acc = np.average(acc_scores)
avg_prec = np.average(prec_scores)
avg_rec = np.average(rec_scores)
# TODO: calculate and print the average accuracy, precision and recall values over all 10 folds
print(f'Average accuracy: {avg_acc} Average precision: {avg_prec} Average recall: {avg_rec}')

# TODO: train the decision tree classifier on entire dataset
final_tree = DecisionTreeClassifier(criterion="entropy", max_depth=3)
final_tree.fit(X, Y)

# TODO: Save the decision tree visualization to disk - replace 'tree' with your decision tree and run the below line
export_graphviz(final_tree, out_file='tree.dot', feature_names = feature_names)
print("DONE")

# TODO: Save the classifier to disk - replace 'tree' with your decision tree and run the below line
print("saving classifier model...")
with open('classifier.pickle', 'wb') as f:
    pickle.dump(tree, f)
# %%
