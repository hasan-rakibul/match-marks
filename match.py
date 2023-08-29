import pandas as pd
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser(description='Compare between two files (csv and xlsx) to check if there are any new marks on the local file.')
    parser.add_argument('--lms', type=str, help='Path to LMS csv file', required=True)
    parser.add_argument('--lms_col_idx', type=int, help='LMS column index to compare with. Index starts from 0.', required=True)
    parser.add_argument('--local', type=str, help='Path to local xlsx file', required=True)
    parser.add_argument('--local_col_idx', type=int, help='Local column index to compare with. Index starts from 0.', required=True)
    
    parser.add_argument('--print_error', type=bool, help='Print error of exception handling', default=False)

    args = parser.parse_args()

    # Reading the files and making the studen_id (col index 2) as the dataframe index
    lms=pd.read_csv(args.lms, index_col=2)
    local=pd.read_excel(args.local, index_col=2)
    
    lms_col = lms.columns[args.lms_col_idx]
    local_col = local.columns[args.local_col_idx]
    
    print('CHECK CAREFULLY!! Comparing Between:')
    print(f'\tLMS column name: {lms_col}')
    print(f'\tLocal column name: {local_col}')
    print('Provide correct lms_col_idx and local_col_idx if they are wrong. Remember col_idx starts from 0. \n')
    
    for row in lms.itertuples():
        try:
            index = int(row.Index)
    
            # making both as float to compare
            lms_mark = float(lms.loc[index, lms_col])
            local_mark = float(local.loc[index, local_col])
            
            if (local_mark is not np.nan) and lms_mark != local_mark:
                '''For empty marks they are NaN and we don't need to proceed if local mark is empty for a student'''
                name = local.loc[index, 'First Name'] + ' ' + local.loc[index, 'Last Name']
                print('\nMismatch found!!!')
                print(f'Student ID: {index}\tMark: {local_mark}\tName: {name}')
        except Exception as e:
            if args.print_error:
                print('\n!!!!! Error !!!!!')
                print(e)
                print(f'Student ID: {row.Index}\n')


if __name__ == '__main__':
    main()