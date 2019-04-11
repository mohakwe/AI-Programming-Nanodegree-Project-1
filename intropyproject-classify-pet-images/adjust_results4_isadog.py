#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Michael Ohakwe
# DATE CREATED: 4/9/2019                                
# REVISED DATE: 4/11/2019
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
# initialize dictionary of dognames
  dognames_dic = {}

# open input file and call it infile
  with open(dogfile, 'r') as infile:

#   Read in a line of the file
    line = infile.readline()
    while line != '':

#     Store the line as the dogname
      dogname = line.rstrip()

#     Populate the dictionary of dognames without repeats
      if dogname not in dognames_dic:
        dognames_dic[dogname] = 1

#     Read in the next line of the file
      line = infile.readline()

# For each image filename
  for key in results_dic:


    if results_dic[key][0] in dognames_dic:

      if results_dic[key][1] in dognames_dic:
#       If the image label is a dogname and the classifier label is a dogname, 
#       then extend the list to include [1,1]
        results_dic[key].extend([1,1])
      elif results_dic[key][1] not in dognames_dic:
#       If the image label is a dogname and classifier label isn't extend with [1,0]
        results_dic[key].extend([1,0])

#
    if results_dic[key][1] in dognames_dic:

        if results_dic[key][0] not in dognames_dic:
#         If only the Classifier label is in the dognames dictionary extend [0,1]
          results_dic[key].extend([0,1])

    elif results_dic[key][1] not in dognames_dic:

        if results_dic[key][0] not in dognames_dic:
#         If neither are in the dognames dictionary extend[0,0]
          results_dic[key].extend([0,0])




    
