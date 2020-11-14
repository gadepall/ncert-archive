"""
Created on Sat Sep 12 22:32:41 2020
Generate 200 random numbers and find probability of each digit
@author: Rubeena
"""
import numpy as np
import pandas as pd

sample_size=200
sample_size2=10000
 
number=np.random.randint(1, 99999999, size=sample_size)
number_second=np.random.randint(1,99999999, size=sample_size2)

#Frequency distribution table as given in the problem in Excel sheet
digit=np.array([0,1,2,3,4,5,6,7,8,9])
Frequency=np.array([22,26,22,22,20,10,14,28,16,20])
freq_given=pd.DataFrame({'Digit':digit,'Frequency':Frequency,'Probability':Frequency/sample_size})
file_locate='Freq_Table_Given.xlsx'
freq_given.to_excel(file_locate,'sheet1',index=False)

def FindFreqTable(unitDigits,digit):          #accordingly check value of frequency of last digit
    freq1=np.zeros((len(digit),),dtype='int')
    for i in range(0,len(unitDigits)):
        for j in range(0,len(digit)):
            if unitDigits[i]==digit[j]:
                c=j
                freq1[c]+=1
    return freq1;

def LastDigitArray(number):
    lastDigit = []
    for i in range(0,len(number)):
        lastDigit.append(number[i]%10)
    return lastDigit;

#Enter Random numbers and their last digits into excel sheet
unitDigits=LastDigitArray(number)
unitDigits_second=LastDigitArray(number_second)

#This part prints frequency of each digit on console.
#Used only for comparison purpose
#frequen=FindFreqTable(unitDigits,digit)
#d2=pd.Series(frequen)
#print("freq of digits of random num generated is \n",d2)

#Generates an excel sheet containing Frequency Distribution Table for Random numbers unit digits
def GenerateFreqTable(digit,unitD,sample_space):
    freq=np.zeros((len(digit),),dtype='int')
    for i in range(0,len(unitD)):
        for j in range(0,len(digit)):
            if unitD[i]==digit[j]:
                c=j
                freq[c]+=1
    return freq;

freq_first=GenerateFreqTable(digit,unitDigits,sample_size)
freq_second=GenerateFreqTable(digit, unitDigits_second,sample_size2)

freq_random_1=pd.DataFrame({"Digit":digit,"Frequency":freq_first,"Probability":freq_first/sample_size})
freq_random_2=pd.DataFrame({"Digit":digit,"Frequency":freq_second,"Probability":freq_second/sample_size2})
filepath = 'Freq_Table_for_200_numbers.xlsx'
filepath2 = 'Freq_Table_for_10000_numbers.xlsx'
freq_random_1.to_excel(filepath,'sheet_random',index=False)
freq_random_2.to_excel(filepath2,'sheet_random_2',index=False)

