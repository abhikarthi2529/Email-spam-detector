# Lets read in the data 

import pandas as pd
import numpy as np
import string


def cleanedData():
    data = pd.read_excel("C:\\Spam Email Classifier\\Project folder\\EmailData.xlsx", usecols=[0, 1])
    cleanText(data, 'text')
    return data

def lowerCase(data, colName):
    data[colName] = data[colName].str.lower()

def removePunctuation(text):
    result = ""
    for char in text:
        if char not in string.punctuation:
            result += char
    return result

def cleanText(data, colName):
    data.dropna(inplace=True)  # This drops any NaN rows in-place
    lowerCase(data, colName)
    for row in range(len(data)):
        text =  data.iloc[row, 0]
        if "subject" in text:
            text = text.replace("subject", "")
        text_without_punctuation = removePunctuation(text)
        data.iloc[row, 0] = text_without_punctuation
        
        


        
    







