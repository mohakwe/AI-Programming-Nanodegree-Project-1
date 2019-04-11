#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Michael Ohakwe
# DATE CREATED: 4/8/19                                 
# REVISED DATE: 4/11/19
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
     """
     Creates a dictionary of pet labels (results_dic) based upon the filenames 
     of the image files. These pet image labels are used to check the accuracy 
     of the labels that are returned by the classifier function, since the 
     filenames of the images contain the true identity of the pet in the image.
     Be sure to format the pet labels so that they are in all lower case letters
     and with leading and trailing whitespace characters stripped from them.
     (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
     Parameters:
     image_dir - The (full) path to the folder of images that are to be
                    classified by the classifier function (string)
     Returns:
          results_dic - Dictionary with 'key' as image filename and 'value' as a 
          List. The list contains for following item:
          index 0 = pet image label (string)
     """
#    List all filenames in the image directory passed into the function
     in_files = listdir(image_dir)

#    Initialize results dictionary
     results_dic = {}

#    Process each filename and extract the image label
     for i in range(0, len(in_files), 1):

#         Initialize variable to store image label
          image_label = "" 

#         Take filename and format it to be stored as image label. Lowercase, no underscores, and everything after '.' removed        
          pet_image = in_files[i]
          pet_image_lower = pet_image.lower()
          pet_image_word_list = pet_image_lower.split('_')
          for word in pet_image_word_list:
               if word.isalpha():
                    image_label += word + ' '                    
          image_label = image_label.strip()

#         Populates the results dictionary with the filename as the key and the formatted image label as the value          
          if in_files[i] not in results_dic:
               results_dic[in_files[i]] = [image_label]
          else:
               print("Duplicate files exist in directory: ", in_files[i])


# Replace None with the results_dic dictionary that you created with this
# function
     return results_dic
