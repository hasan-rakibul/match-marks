import pandas as pd
import math
from colorama import Back
import logging
import json

logging.basicConfig(
    format='%(levelname)s - %(message)s',
    level=logging.INFO
)

def _menu(mapping_json: str) -> tuple:
    with open(mapping_json, "r") as f:
        mapping = json.load(f)

    # generate the menu
    options = list(mapping.keys())
    menu = input(
        "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)]) + "\n"
        + "Choose what you want to update: "
    ).strip()

    try:
        selected_option = options[int(menu)-1] # 1-based to 0-based
        lms_col = mapping[selected_option]['lms_col']
        local_col = mapping[selected_option]['local_col']
    except (ValueError, IndexError):
        logging.info('Invalid option. Exiting...')
        lms_col, local_col = None, None
        
    return lms_col, local_col

def main():
    mapping_json = "mapping.json"
    lms_col, local_col = _menu(mapping_json)
    if lms_col is None or local_col is None:
        return

    lms_file = input("LMS CSV file (default: lms.csv): ").strip() or "lms.csv"
    local_file = input("Local XLSX file (default: local.xlsx): ").strip() or "local.xlsx"

    # Reading the files and making the usernames (col index 3) as the dataframe index. Some student ID are empty, so using username
    lms=pd.read_csv(lms_file, index_col=3)
    local=pd.read_excel(local_file, index_col=3)
    
    # convert the index dtype to str; there was a mismatch between lms and local
    local.index = local.index.map(str)
    lms.index = lms.index.map(str)
    
    # input: nth column whereas python is 0-based. Plus, I will make student_id as index (so, one column index is vanished there)
    lms_col = lms.columns[lms_col-2]
    local_col = local.columns[local_col-2]

    logging.info('CHECK CAREFULLY!! Comparing Between:')
    logging.info('LMS column name: ' + Back.YELLOW + lms_col + Back.RESET)
    logging.info('Local column name: ' + Back.YELLOW + local_col + Back.RESET)

    # print the maximum marks in local file
    # it may be useful to know if the marks are in the correct range
    min_mark = local[local_col].apply(pd.to_numeric, errors="coerce").min()
    max_mark = local[local_col].apply(pd.to_numeric, errors="coerce").max()
    logging.info('Range of mark in local file: ' + \
                 Back.GREEN + str(min_mark) + " - " + str(max_mark) + Back.RESET)

    is_right = input('All good to proceed? (y[default]/n): ') or 'y' # default is yes
    if is_right.lower() != 'y' and is_right.lower() != 'yes':
        logging.info('Exiting...')
        return

    for row in lms.itertuples():
        if row.Index not in local.index:
            logging.debug(f"Student ID {row.Index} is not in local file. Skipped.")
            continue
        # convert marks to float
        try:
            local_mark = float(local.loc[row.Index, local_col])
        except:
            logging.info(Back.RED + "Student ID " + row.Index + " has invalid mark formatting in local file: " + local.loc[row.Index, local_col] + ". Skipped." + Back.RESET)
            continue
        
        # empty marks are NaN
        # sometimes when some marks are only on LMS, we don't need to proceed if local mark is empty for a student
        if math.isnan(local_mark):
            logging.debug(f"Student ID {row.Index} has probable empty mark in local file: {local_mark}. Skipped.")
            continue
        
        lms_mark = lms.loc[row.Index, lms_col]
        if type(lms_mark) == str:
            if lms_mark == 'In Progress' or lms_mark == 'Needs Marking': # Those who submitted in LMS
                logging.debug(f"Student ID {row.Index} has invalid marking in LMS file: {lms_mark}. Considered as 0.")
                lms_mark = 0.0
            elif lms_mark[:13] == 'Needs Marking': # those who submitted after their marks are uploaded in LMS, marks would be 'Needs Marking(<marks>)'
                lms_mark = lms_mark[14:-1] # extracting the marks. 13th is '(' and the end has ')'

        lms_mark = float(lms_mark)
        
        if math.isnan(lms_mark):
            logging.debug(f"Student ID {row.Index} has empty mark in LMS file: {lms_mark}. Considered as 0.")
            lms_mark = 0.0

        if lms_mark < local_mark:
            lastname = lms.loc[row.Index, 'Last Name']
            firstname = lms.loc[row.Index, 'First Name']
            lms.loc[row.Index, lms_col] = local_mark
            logging.info(f"{lastname}, {firstname} ({row.Index}): {lms_mark} --> {local_mark}. Updated.")
        elif lms_mark > local_mark:
            logging.info(f"Student ID {row.Index} has higher mark in LMS file: {lms_mark} > {local_mark}. Skipped.")

    save_as = "lms_updated.csv"    
    lms.to_csv(save_as, index=False)
    logging.info(f"Updated LMS file saved as {save_as}")

if __name__ == '__main__':
    main()