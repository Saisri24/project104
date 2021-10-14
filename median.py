import csv;

with open('data.csv', newline='') as data:
    reader = csv.reader(data)
    filedata = list(reader)

filedata.pop(0)
weight_of_all = []

for i in range(len(filedata)):
    weight = filedata[i][2]
    weight_of_all.append(float(weight))

weight_of_all.sort()
n = len(weight_of_all)
if len(weight_of_all) % 2 == 0:
    n1 = float(weight_of_all[n // 2])
    n2 = float(weight_of_all[n // 2 - 1])
    median = (n1 + n2) / 2 
else:
    median = float(weight_of_all[n // 2])

print(median)