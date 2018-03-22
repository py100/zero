#coding=utf8
import sys
sys.path.append('..')
import utility.utility

def main():
    tables, folder_to_process = utility.utility.load_conf('../../config/')
    for folder in folder_to_process:
        for table in tables:
            utility.utility.datafilter(table, folder, '../../../data/2016-11-01/')

if __name__ == '__main__':
    main()
