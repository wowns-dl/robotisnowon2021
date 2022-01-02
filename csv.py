import csv

f = open('C:\Temp\dum.csv', encoding = 'utf-8', newline = '')
data = csv.reader(f)
header = next(data)

max_data = -273.15
max_temp = 0

for i in data:    
    i[4]=float(i[4])
    if max_data < i[4]:
        max_data = i[4]

print(max_data)

f.close()


#print('기온이 가장 높았던 날은',max_data,'로',max_temp,'도 였습니다.')
