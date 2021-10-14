from collections import Counter #counter counts the amount of times a number is shown
import csv
with open("data.csv", newline = "") as f : #opens data.csv as f
    reader = csv.reader(f)   #reads
    file_data = list(reader) #puts all what was read into file_data

file_data.pop(0) #remove the titles from the data

new_data = [] #empty list

for i in range(len(file_data)) : #gest the elements inside the list
    n_num = file_data[i][1] #each element
    new_data.append((n_num))  #puts the data from file_data to new_data 

data = Counter(new_data)
mode_data_for_range = { #creating three categories and putting the count of each of the values in them 
#its 0 because right now the counts are zero since none of the values were looked at
    "50-60" : 0, 
    "60-70" : 0,
    "70-80" : 0,
}

#every time it looks through a value it will place that value in one of the categories and increase that category's count by one
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurence


mode_range, mode_occurence = 0,0 #mode range and mode occurence both are set to 0
for range, occurence in mode_data_for_range.items(): #using the for loop on the items
    if occurence > mode_occurence: #occurence is the three categories
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
        #using the range.split we get the first and the second number mode

mode = float((mode_range[0] + mode_range[1]) / 2) #this is the mean of the two modes
print("mode is -> " +str(mode))