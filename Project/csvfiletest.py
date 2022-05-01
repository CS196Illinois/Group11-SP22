import csv
import random

header = ['Name', 'Score']
names = ['John','Sandy','Coco','Snute','Noel','Monsoon','Eric','Allen','Michelle','Cathy']
data = []

for i in range(1000):
  data.append([random.choice(names), random.randint(1, 100)])

with open('./output.csv', 'w', encoding='UTF8', newline='') as f:
  # create the csv writer
  writer = csv.writer(f)
  
  writer.writerow(header)
  writer.writerows(data)

# close the file
f.close()


