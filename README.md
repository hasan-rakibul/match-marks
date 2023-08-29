# match-marks

The idea is to compare between two columns (students' marks) for each student ID.
It compares between two files (csv and xlsx) to check if there are any new marks on the local file.

## Usage

```
python3 match.py --lms <lms_file.csv> --lms_col <LMS_COL> --local <local_file.xlsx> --local_col <LOCAL_COL> [--print_exception <True/False>]
```

## Options

```
  -h, --help          show this help message and exit
  --lms               Path to LMS csv file
  --lms_col           LMS column index to compare with. Index starts from 0.
  --local             Path to local xlsx file
  --local_col         Local column index to compare with. Index starts from 0.
  --print_exception   Print error of exception handling
```