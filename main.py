import pandas as pd
import math
import argparse
from colorama import Back

def main():
    parser = argparse.ArgumentParser(description='Compare between two files (csv and xlsx) to check if there are any new marks on the local file.')
    parser.add_argument('--lms', type=str, help='Path to LMS csv file', required=True)
    parser.add_argument('--lms_col', type=int, help='nth LMS column to compare with', required=True)
    parser.add_argument('--local', type=str, help='Path to local xlsx file', required=True)
    parser.add_argument('--local_col', type=int, help='nth local column to compare with', required=True)

    args = parser.parse_args()

    # Reading the files and making the usernames (col index 3) as the dataframe index. Some student ID are empty, so using username
    lms=pd.read_csv(args.lms, index_col=3)
    local=pd.read_excel(args.local, index_col=3)

    # convert the index dtype to str; there was a mismatch between lms and local
    local.index = local.index.map(str)
    lms.index = lms.index.map(str)
    
    # input: nth column whereas python is 0-based. Plus, I will make student_id as index (so, one column index is vanished there)
    lms_col = lms.columns[args.lms_col-2]
    local_col = local.columns[args.local_col-2]
    
    print('CHECK CAREFULLY!! Comparing Between:')
    print('\tLMS column name: ' + Back.YELLOW + lms_col + Back.RESET)
    print('\tLocal column name: ' + Back.YELLOW + local_col + Back.RESET)
    print('Provide correct lms_col and local_col if they are wrong. Remember they start from 1. \n')

    common_index = lms.index.intersection(local.index)

    for index in common_index:
        # convert marks to float

        local_mark = float(local.loc[index, local_col])
        
        # empty marks are NaN
        # sometimes when some marks are only on LMS, we don't need to proceed if local mark is empty for a student
        if math.isnan(local_mark):
            continue
        
        lms_mark = lms.loc[index, lms_col]

        if type(lms_mark) == str:
            if str(lms_mark) == 'nan' or lms_mark == 'In Progress' or lms_mark == 'Needs Marking': # empty (nan) or those who submitted in LMS
                lms_mark = 0.0
            elif lms_mark[:13] == 'Needs Marking': # those who submitted after their marks are uploaded in LMS, marks would be 'Needs Marking(<marks>)'
                lms_mark = lms_mark[14:-1] # extracting the marks. 13th is '(' and the end has ')'

            lms_mark = float(lms_mark)

        if lms_mark != local_mark:
            lastname = lms.loc[index, 'Last Name']
            firstname = lms.loc[index, 'First Name']
            print('\n\tMismatch found!!!')
            print(f'Student ID: {index}\tMark: {local_mark}\tLast Name: {lastname}\tFirst Name: {firstname}')

if __name__ == '__main__':
    main()