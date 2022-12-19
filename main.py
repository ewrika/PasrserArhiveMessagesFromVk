from collections import OrderedDict
import os
import re

def ParserAllTxtToStroki():
    clas = 'https://sun9'
    a=0
    b=0

    with open(f"all1.txt", "r") as file1:
        lines = file1.readlines()

    with open("stroki.txt", "a") as file:
        for i in lines:
            a += 1
            if clas in i:
                b += 1
                file.write(str(i) + '\n')
        file.write('Первый Файл закончен\n')
    print("Первый файл Закончен")
    print("Прочитано строк в первом файле " + str(a))
    print("Записано  строк в первом файле " + str(b*2))
    file1.close()
    file.close()
def udalenie_strok():
    filename = 'stroki.txt'
    with open(filename) as file:
        uniq = OrderedDict.fromkeys(file)
    with open(filename, 'w') as file:
        file.writelines(uniq)

def Udalenie_attributov():
    f = open("stroki.txt", "rt")
    inputfilecontents = f.read()
    newline = re.sub("<a class='attachment__link'", "", inputfilecontents)
    f = open("stroki.txt", "w")
    f.write(newline)

def Udalenie_attributov2():
    f = open("stroki.txt", "rt")
    inputfilecontents = f.read()
    newline = re.sub("href='", "", inputfilecontents)
    f = open("stroki.txt", "w")
    f.write(newline)

def Dopisivanie_Attributov():
    text = '<a href="site.ru/link"><img src="'  # фраза, которая будет дописана в начало строки
    output = ''  # инициализация результирующего текста
    count=0

    with open('stroki.txt', 'r') as file:
        for line in file:  # считывание текущего файла
            output += (text + line.replace('\n', '')+'\n')
            count+=1
        print(count)
    with open('stroki.txt', 'w') as file:
        file.write(output)  # перезапись файла

def Dopisivanie_Attributov1_1():
    import re
    sep = "'"
    output = ''
    with open("stroki.txt", 'r') as file:
        for line in file:
            output += (line.split(sep, 1)[0] + '\n')
    with open("stroki.txt", 'w') as file:
        file.write(output)


def Dopisivanie_Attributov2():
    text = '" >/></a>'  # фраза, которая будет дописана в конец строки
    output = ''  # инициализация результирующего текста
    count = 0

    with open('stroki.txt', 'r') as file:
        for line in file:  # считывание текущего файла
            output += (line.replace('\n', '') + text + '\n')
            count += 1
        print(count)

    with open('stroki.txt', 'w') as file:
        file.write(output)  # перезапись файла

def Sozdanie_html():
    text = """  <html>
<head>
     <title>Hello World!</title>
</head>
<body>
     Hello World!\n """

    with open('test.txt', 'w') as file:
        file.write(text)  # перезапись файла

def soedinenie_filof():
    filenames = ['stroki.txt']
    with open('final.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    print('Файлы Соединены ')



def konec_file():
    text="""
    </body>
</html>
    
    """
    file = open('final.txt', "a")
    file.write(text)

def udalenie_musora():
    if os.path.isfile('stroki.txt'):
        os.remove('stroki.txt')
        print("success")
    else:
        print("File doesn't exists!")

    if os.path.isfile('test.txt'):
        os.remove('test.txt')
        print("success")
    else:
        print("File doesn't exists!")

def TxtToHmtl():
    os.rename('final.txt', 'final.html')




def AllhtmlToTxt():
    try:
        count = 0
        print('Изменяю разрешения у всех html to txt')
        while count >= 0:
            os.rename(fr'messages{count}.html', fr'messages{count}.txt')
            count += 50
            print(count)
    except FileNotFoundError:
        pass

def Sozdanie_all1():
    try:
        i = 0
        ii = 50
        print('Начал Совмещать все messages.txt в один all1.txt')
        while i >= 0:
            print(i, " ", ii)
            filenames = [fr'messages{i}.txt', fr'messages{ii}.txt']
            with open('all1.txt', 'a') as outfile:
                for fname in filenames:
                    i += 50
                    ii += 50
                    with open(fname) as infile:
                        for line in infile:
                            outfile.write(line)
    except FileNotFoundError:
        pass
AllhtmlToTxt()
Sozdanie_all1()
Sozdanie_html()
ParserAllTxtToStroki()
udalenie_strok()
Udalenie_attributov()
Udalenie_attributov2()
Dopisivanie_Attributov()
Dopisivanie_Attributov1_1
Dopisivanie_Attributov2()
soedinenie_filof()
konec_file()
udalenie_musora()
TxtToHmtl()