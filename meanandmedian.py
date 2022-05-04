import csv

with open('India_population.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

length_of_data = len(new_data)

total = 0

for x in new_data:
    total += x

mean = round(total/length_of_data)

print("The Mean(Average) is : " + str(mean))

new_data.sort()

if length_of_data%2 == 0:
    median1 = float(new_data[length_of_data//2])
    median2 = float(new_data[length_of_data//2 - 1])
    median = round((median1+median2)/2)

else:
    median = round(float(new_data[length_of_data/2]))

print("The Median is : " + str(median))

