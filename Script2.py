# -*- coding: cp1251 -*-
from fuzzywuzzy import fuzz
with open("C:/Users/Kiril/Downloads/script2log.log", 'r', encoding='utf-8') as f: #Замените путь к лог файлу на свой
    list_of_lines = f.readlines()
with open ("C:/Users/Kiril/Downloads/aruco_detect_server-1script2.log", 'r', encoding='utf-8') as g: #Замените путь к лог файлу c aruco-маркерами на свой
    list_of_lines2=g.readlines()
c=0
check=[]
endlist=[]
for x in range (len(list_of_lines2)):
    d=x*2+1
    string1 = list_of_lines2[x]
    string2 = 'Have marker result' # Откройте лог файл, и посмотрите, какой строкой отменачется подъезд к маркеру, её и вставьте в эту строку
    z = int(fuzz.partial_ratio(string1,string2))
    splitstring = string1.split()
    try:
        splitstring2 = list_of_lines[d].split()
    except:
        continue
    count = 0
    if z == 100:
        for q in range (len(check)):
            if int(check[q]) == int(splitstring[-1]):
                count = count + 1
        if count == 0:
            z = int(splitstring[-1])
            check.append(z)
            c=c+1
            d = str(c)
            string3 = "painting " + d + " " + splitstring[-1] + ''
            for p in range (len(splitstring2)-5):
                string3 = string3 + " " + splitstring2[p+5]
            endlist.append(string3)
file = open("C:/Users/Kiril/Desktop/1.txt", "w")
for b in range (len(endlist)):
    file.write(str(endlist[b]))
    file.write('\n')
file.close()