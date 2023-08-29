# match-marks

The idea is to compare between two columns (students' marks) for each student ID.
It compares between two files (csv and xlsx) to check if there are any new marks on the local file.

## Usage
`python3 match.py --lms <lms_file.csv> --lms_col_idx <LMS_COL_IDX> --local <local_file.xlsx> --local_col_idx <LOCAL_COL_IDX> [--print_error <True/False>]`

## Options
```
  -h, --help            show this help message and exit
  --lms LMS             Path to LMS csv file
  --lms_col_idx LMS_COL_IDX
                        LMS column index to compare with. Index starts from 0.
  --local LOCAL         Path to local xlsx file
  --local_col_idx LOCAL_COL_IDX
                        Local column index to compare with. Index starts from 0.
  --print_error PRINT_ERROR
                        Print error of exception handling
```