import csv
import re
import sys

class ReaderCSV:
    def __init__(self, filepath:str):
        self.filepath = filepath
        self.csvDataList = list()

    def readCSV(self):
        if(re.search('\.csv$', self.filepath) != None):
            try:
                with open(self.filepath, encoding='UTF8') as csvfile:
                    csvData = csv.reader(csvfile)
                    for d in csvData:
                        self.csvDataList.append(str(d))
                return self.csvDataList
            except FileNotFoundError:
                print(f"File {self.filepath} not found.")
                sys.exit(1)
            except OSError:
                print(f"OS error ocurred trying to open {self.filepath}")
                sys.exit(1)
            except Exception as err:
                print(f"Unexpected error opening {self.filepath} is", repr(err))
                sys.exit(1)
        else:
            raise IOError('Wrong file extension, use .csv')