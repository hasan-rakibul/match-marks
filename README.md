# match-marks

The idea is to compare between two columns (students' marks) for each student ID.
It compares between two files (csv and xlsx) to check if there are any new marks on the local file.

## Usage
Configure filenames and run:
```
./match_mark.sh
```
It will ask for `lms_col` and `local_col`. Alternatively, you can pass them as arguments:

```
python3 match.py --lms <lms_file.csv> --lms_col <LMS_COL> --local <local_file.xlsx> --local_col <LOCAL_COL>
```

The output will be sorted by last name.

## Options

```
  -h, --help          show this help message and exit
  --lms               Path to LMS csv file
  --lms_col           nth LMS column to compare with
  --local             Path to local xlsx file
  --local_col         nth Local column to compare with
```