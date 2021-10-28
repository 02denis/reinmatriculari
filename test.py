import csv
import re
import os
from difflib import SequenceMatcher

#dicționar pentru materiile din anul 1 / șablon
dct_an1={
    'Algoritmi si structuri de date I':[28, 28, -1, 6],
    'Programare I':[28, 28, -1, 6],
    'Logică computationala':[28, 28, -1, 6],
    'Algebra si geometrie analitica':[28, 28, -1, 5],
    'Calcul diferential si integral':[28, 28, -1, 5],
    'Algoritmi si structuri de date II':[28, 28, -1, 6],
    'Arhitectura calculatoarelor':[28, 28, -1, 5],
    'Programare II':[28, 42, -1, 6],
    'Limbaje formale si teoria automatelor':[28, 28, -1, 5],
    'Elemente de web design / Metode si practici in informatica':[28, 14, -1, 4],
    'Stagiu de practica I':[0, 14, -1, 2],
    'Limba straina 1':[14, 14, -1, 2],
    'Limba straina 2':[14, 14, -1, 2],
    'Educatie fizica si sport 1':[0, 28, -1, 1],
    'Educatie fizica si sport 2':[0, 28, -1, 1],
    }


lst=[]
def open1(): #citim din fisier si formam o lista cu fiecare rand
    with open(r'C:\\Users\\denii\\Desktop\\Popescu.csv','rt', encoding='UTF8') as f:
        data = csv.reader(f)
        for i in data:
            lst.append(str(i))


open1()

#CAUTAM NUMELE STUDENTULUI
lista_nume=lst.copy()
numele=[]
for i in range(len(lista_nume)):
    lista_nume[i]=re.sub(';',' ',lista_nume[i])
    lista_nume[i]=re.sub(' +',' ',lista_nume[i])
    lista_nume[i]=lista_nume[i].split()
    for j in range(len(lista_nume[i])):
        if "timpul" in lista_nume[i][j]:
            #print(lista_nume[i])
            for dd in range(len(lista_nume[i])):
                if re.match(r'[^\W\d_]',lista_nume[i][dd]):
                    numele.append(lista_nume[i][dd])
for i in range(len(numele)):
    if re.match("de:",numele[i]):
        indexx=i
        break
nume_complet=str()
for i in range(indexx+1, len(numele)-1):
    nume_complet=nume_complet+numele[i]+" "
#print(nume_complet)
#CAUTAM FIECARE APARITIE A MATERIILOR, FOLOSINDU-NE DE NR.CRT - MATERIILE SUNT NUMEROTATE
#SUB FORMA DE LISTA DE LA 1-19 MAXIM
#print(lst)
newl=list()
for i in range(1,20):
    caut=re.compile(".*;;"+str(i)+";(;)?([a-zA-Z])")
    newl.append(list(filter(caut.match,lst)))
#print(newl)

#SALVAM FIECARE LISTA INTR-UN DICTIONAR CU MATERII + NOTELE
dct={}
dct2={}
dct3={}
for i in range(len(newl)):
    for j in range(len(newl[i])):
        strr=str()
        newl[i][j]=re.sub(';',' ',newl[i][j]) #sterg toate aparitiile ; , si " " in plus
        newl[i][j]=re.sub(' +',' ',newl[i][j])
        parts=newl[i][j].split(" ")   
        ok=0
        for d in range(2,len(parts)):
            if re.match("[a-zA-Z]",parts[d]) and (len(parts[d])>1):
                strr=strr+parts[d]+' '
        strr=strr[:-1] #sterg spatiul in plus de la sf materiei
        for d in range(2,len(parts)):
            if re.match("[1-6]",parts[d]):
                semestru=int(parts[d])
                break
        if semestru == 1 or semestru == 2:
            if strr not in dct:
                dct[strr]=parts[len(parts)-2]
            else:
                strr=strr+' '+str(semestru)
                dct[strr]=parts[len(parts)-2]
        elif semestru == 3 or semestru == 4:
            if strr not in dct2:
                dct2[strr]=parts[len(parts)-2]
            else:
                strr=strr+' '+str(semestru)
                dct2[strr]=parts[len(parts)-2]
        else:
            dct3[strr]=parts[len(parts)-2]
#if dct:
 #   print("ANUL I")
  #  for key, value in dct.items():
   #     print(key, value)
    #print(end="\n")
#if dct2:
 #   print("ANUL II")
  #  for key, value in dct2.items():
   #     print(key, value)
    #print(end="\n")
#if dct3:
 #   print("ANUL III")
  #  for key, value in dct3.items():
   #     print(key, value)

print(nume_complet)

lst_grades=[]
lst_grades2=[]

def verify_cls(materie1,materie2):
    if SequenceMatcher(None,(materie1),(materie2)).ratio()>0.6: #100%
        if re.match("1",str(materie1[len(materie1)-1])) and not re.match("2",str(materie2[len(materie2)-1])):
            return True
        elif re.match("2",str(materie1[len(materie1)-1])) and re.match("2",str(materie2[len(materie2)-1])):
            return True
        elif re.search("I",str(materie1[len(materie1)-1])) and not re.search("II",str(materie2)):
            return True
        elif re.search("II",str(materie1)) and re.search("II",str(materie2)):
            return True
        elif re.match(r'[^\W\d_]',str(materie1[len(materie1)-1])) and re.match(r'[^\W\d_]',str(materie2[len(materie2)-1])) and not re.match("I",str(materie1[len(materie1)-1])):
            return True
        elif re.match(r'[^\W\d_]',str(materie1[len(materie1)-1])) and re.match(r'[^\W\d_]',str(materie2[len(materie2)-1])) and not re.match("I",str(materie2[len(materie2)-1])):
            return True
    return False

    
for key, value in dct_an1.items():
    for keyy, valuee in dct.items():
        #if SequenceMatcher(None, key, keyy).ratio()>0.5:
            if verify_cls(key,keyy):
                value[2]=dct[keyy]
                #print(key, value)

def new_csv(): #formam un fisier csv nou cu numele studentului
    username = os.getlogin()
    name=nume_complet
    with open(f'C:\\Users\\{username}\\Desktop\\{name}.csv','w') as file:
        writer = csv.writer(file)

new_csv()

def write_new_csv():
    data=[]
    username = os.getlogin()
    name=nume_complet
    with open(f'C:\\Users\\{username}\\Desktop\\{name}.csv','w', encoding='UTF8', newline='') as file:
        writer=csv.DictWriter(file, fieldnames=["Disciplina promovată cf. planului de învăţământ al promoţiei cu care s-a înmatriculat în anul I","C","S/L","Nota","Credite","Disciplina echivalată din planul de învăţământ al promoţiei în care se reînmatriculează","CU","SE/LA","Not.","Cred."])
        writer.writeheader()
        for key, value in dct_an1.items():
            if not re.match("[0-4]",str(value[2])):
                writer.writerow({'Disciplina promovată cf. planului de învăţământ al promoţiei cu care s-a înmatriculat în anul I':key,'C':value[0],'S/L':value[1],'Nota':value[2],'Credite':value[3],"Disciplina echivalată din planul de învăţământ al promoţiei în care se reînmatriculează":key,'CU':value[0],'SE/LA':value[1],'Not.':value[2],'Cred.':value[3]})
            else:
                writer.writerow({"Disciplina echivalată din planul de învăţământ al promoţiei în care se reînmatriculează":key,'CU':value[0],'SE/LA':value[1],'Not.':'','Cred.':value[3]})
write_new_csv()
