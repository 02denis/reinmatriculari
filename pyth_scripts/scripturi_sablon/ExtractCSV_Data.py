import re 
from difflib import SequenceMatcher

class ExtractDataFromCSV:
    def __init__(self, csvDataList:list()):
        numele_studentului = ""
        lista_dictionare_materii = []
        self.csvDataList = csvDataList #raw data csv sablon
        self.lista_dictionare_ani = list()
    
    def get_student_name(self):
        numele = []
        csvDataListCopy = self.csvDataList.copy()
        for i in range(0, len(csvDataListCopy)):
            csvDataListCopy[i]=re.sub(';',' ',csvDataListCopy[i])
            csvDataListCopy[i]=re.sub(' +',' ',csvDataListCopy[i])
            csvDataListCopy[i]=csvDataListCopy[i].split()
            for j in range(len(csvDataListCopy[i])):
                if "timpul" in csvDataListCopy[i][j]:
                    #print(csvDataListCopy[i])
                    for dd in range(len(csvDataListCopy[i])):
                        if re.match(r'[^\W\d_]',csvDataListCopy[i][dd]):
                            numele.append(csvDataListCopy[i][dd])
        for i in range(len(numele)):
            if re.match("de:",numele[i]):
                indexx=i
                break
        nume_complet=str()
        for i in range(indexx+1, len(numele)-1):
            nume_complet=nume_complet+numele[i]+" "
        return nume_complet

    def get_materii(self):
        newl=list()
        for i in range(1,20):
            caut=re.compile(".*;;"+str(i)+";(;)?([a-zA-Z])")
            newl.append(list(filter(caut.match,self.csvDataList)))

        dct={}
        dct2={}
        dct3={}
        for i in range(len(newl)):
            for j in range(len(newl[i])):
                strr=str()
                newl[i][j]=re.sub(';',' ',newl[i][j]) #sterg toate aparitiile ; , si " " in plus
                newl[i][j]=re.sub(' +',' ',newl[i][j])
                parts=newl[i][j].split(" ")   

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

        if dct:
            self.lista_dictionare_ani.append(dct)
        if dct2:
            self.lista_dictionare_ani.append(dct2)
        if dct3:
            self.lista_dictionare_ani.append(dct3)
        
        return self.lista_dictionare_ani
    

