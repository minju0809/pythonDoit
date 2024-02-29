import os, re
import usecsv
os.chdir(r'C:\Users\kmj\Desktop\coding\python')

apt = usecsv.switch(usecsv.opencsv('apt202402.csv'))
print(apt[:2])  # apt의 처음 2개 요소 출력
print(len(apt))  # apt의 길이 출력

# for i in apt[:6]:
#   print(i[1], i[6], i[7], i[10], i[11])

new_list = []

for i in apt[:1]:
  new_list.append([i[1], i[6], i[7], i[10], i[11]])
for i in apt:
    try:
        if float(i[10]) <= 5000 and float(i[11]) <= 50 and re.search('관악', i[1]):
            print(i[1], i[6], i[7], i[10], i[11])
            new_list.append([i[1], i[6], i[7], i[10], i[11]])
    except ValueError: 
        pass
    
usecsv.writecsv('lower5000_lower50.csv', new_list)