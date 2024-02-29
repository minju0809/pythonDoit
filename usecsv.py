import csv, os

def opencsv(filename):
  f = open(filename, 'r', encoding='cp949')
  reader = csv.reader(f)
  output = []
  for i in reader:
      output.append(i)
  return output

def writecsv(filename, the_list):
  with open(filename, 'w', newline = '', encoding='cp949') as f:
    a = csv.writer(f, delimiter=',')
    a.writerows(the_list)

def switch(listName):
  for i in listName:
    for j in i:
      try:
          i[i.index(i)] = float(j.replace(',', ''))
      except:
          pass
  return listName