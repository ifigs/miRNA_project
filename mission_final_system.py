#
# Project Submission for Let's Hack Cancer
# Isabela Figueira
# Final System
#
# TO RUN: with a spefic sample, edit the last of the code to input a different data sample.
#
# Can follow my method of importing csv files and converting the subsequent dataframes to a list and then run with my method as well
#

import numpy as np
import pandas as pd


#import the data into pandas dataframes
df_clinical = pd.read_csv("datasets/clinical.csv") 
df_RNA = pd.read_csv("datasets/miRNA_counts.csv") 

#merge the two dataframes on the patient id. one of the sets has slightly more patients, so that will get cut
merged_inner = pd.merge(left=df_clinical,right=df_RNA, left_on='patient_id', right_on='patient_id')

#get the target values out
#remove the clinical data. we just used the clinical data to match the patient ids and remove stragglers 
#drop the patient id as well

#the miRNA data
total_data = merged_inner.drop(['patient_id','gender', 'year_of_birth', 'race', 'vital_status', 'ethnicity',
                   'year_of_diagnosis', 'primary_diagnosis', 'tumor_stage',
                   'age_at_diagnosis', 'prior_treatment', 'tissue_or_organ_of_origin',
                   'prior_malignancy', 'ajcc_pathologic_stage',
                   'site_of_resection_or_biopsy', 'treatment_type',
                   'treatment_or_therapy'], axis=1)

# shuffle the data for future machine learning
shuffled = total_data.sample(frac=1)

# The frac keyword argument specifies the fraction of rows to return in the random sample,
# so frac=1 means return all rows (in random order)

y_data = shuffled['cancer']

x_data = shuffled.drop('cancer',axis=1)




#Given one sample, return the list of likeliest cancers
#since we don't need to worry about efficiency as much here, since we have only one sample to compare,
#we revert to the original method.

xdata = np.array(x_data)
ydata = np.array(y_data)

def predict_cancer_type(sample):
    #the sample should be an array of length 1881, which is the feature size
    if(len(sample) != 1881):
        print("length of array should be 1881 features")
        return -1
    sample = np.array(sample)
    
    p = 0.4 #what kind of sensitivity for distance. 2 is euclidean distance
    
    #The Minkowski distance is a metric in a normed vector space which can be considered 
    # as a generalization of both the Euclidean distance (p=2) and the Manhattan distance (p=1).
    
    probs = { "lung": -1, "prostate":-1, "endometrial":-1,"colorectal":-1,"kidney":-1   }    
    
    for j in range(0,len(xdata)):
        y_current = y_data[j]
        #distance = minkowski_distance(sample, xdata[j], p)
        
        distance = np.sum(np.abs(sample - xdata[j])**p, axis=-1)
        if probs[y_current] == -1:
            probs[y_current] = distance
        elif distance < probs[y_current]:
            probs[y_current] = distance

    #sort the probabilities by smallest to largest
    #and only print out the top 3 likeliest 
    p_view = [ (v,k) for k,v in probs.items() ]
    p_view.sort(reverse=False) #sort tuples by first element
    #for v,k in p_view[0:3]:
    #    print("%s: %f" % (k,v))
    
    print("The top three cancer types closest to the given sample, in order from least to largest distance")
    print("1. %s" % p_view[0][1])
    print("2. %s" % p_view[1][1])
    print("3. %s" % p_view[2][1])
        
    return p_view[0:3]

#example of it working:        
predict_cancer_type(xdata[2])


