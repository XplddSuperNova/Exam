#pip3 install fuzzywuzzy[speedup] 
from fuzzywuzzy import fuzz
with open("C:/Users/Kiril/Downloads/test.log") as f: #Замените путь к лог файлу на свой
    list_of_lines = f.readlines()
c=0
for x in range (len(list_of_lines)):
    string1 = list_of_lines[x]
    string2 = 'reached Painting 8' # Откройте лог файл, и посмотрите, как ойстрокой заканчивается цикл, её и вставьте в эту строку
    z = int(fuzz.partial_ratio(string1,string2))
    if z == 100:
        c=c+1
print(c)