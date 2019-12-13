# miRNA_project

Introduction:

For my project I worked on the Hack Cancer Deep Genomics Mission  from the company Quantgene. They are working to leverage liquid biopsy and cfDNA to detect mutational patterns of cancer in the blood. This technology will allow physicians to screen for cancer at early stages. 

The goal of the Mission is to create a descriptive pattern-matching system that uses their Deep Genomics dataset to match a new sample against the existing empirical dataset samples and get a clear insight which category of cancer matches best with a new sample. This problem boils down to multiclass classification. There are five kinds of cancer diagnoses in this dataset (colorectal, prostate, endometrial, kidney, lung), and the objective is to predict what the label is given patient data consisting of expression values of miRNA.

Files included in my project:

- project_course_final.ipynb: this file contains my course project for ics184a in which I compare the leave one out method for the hackathon and other multiclass classification algorithms.

- project_hack.ipynb: the jupyter notebook I submitted to the hackathon

- mission_final_system.py: the final system requested by the hackathon that takes in one sample as input and returns a ranked list of the most likely cancer labels to match the given sample

- datasets: contains the csv files with the data as well as dataset description

- gene_project-data_processing.ipynb: initial data processing and analysis before experimenting with my methods

- decision_tree.pdf: visualization of the decision tree algorithm implemented

