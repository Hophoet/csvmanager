import pandas as pd
from csv import DictReader
from csv_diff import load_csv, compare
import csv
import copy


class CSV:
    """ CSV files management class """
    @classmethod
    def is_a_valid_csv_file(cls, file):
        pass

    @classmethod
    def files_are_same_columns(cls, file1, file2):
        fileone = copy.deepcopy(file1).readlines()
        filetwo = copy.deepcopy(file2).readlines()
        fileone_columns = fileone[0].decode().split(',')
        filetwo_columns = filetwo[0].decode().split(',')
        # check the same colums size of the files
        if len(fileone_columns) != len(filetwo_columns):
            return False
        same_columns = True
        # check if the files have the same columns name
        for index in range(len(fileone_columns)):
            if fileone_columns[index] != filetwo_columns[index]:
                print('difference',
                      fileone_columns[index], filetwo_columns[index])
                return False
        return same_columns

    @classmethod
    def get_difference(cls, file1, file2):
        fileone = file1.readlines()
        filetwo = file2.readlines()
        columns = fileone[0]
        with open('csvs/update.csv', 'w') as outFile:
            outFile.write(columns.decode())
            for line in filetwo:
                if line not in fileone:
                    line = line.decode()
                    outFile.write(line)
            for line in fileone:
                if line not in filetwo:
                    line = line.decode()
                    outFile.write(line)
