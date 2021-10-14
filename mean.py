import csv

with open('data.csv', newline='') as data:
    reader = csv.reader(data)
    filedata = list(reader)

filedata.pop(0)

weight_of_all = []

for i in range(len(filedata)):
    weight = filedata[i][2]
    weight_of_all.append(float(weight))

l = len(weight_of_all)
total = 0

for i in weight_of_all:
    total = total + i

mean = total / l

print(mean)