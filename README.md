# match-marks
Assuming you have a local copy of students' marks in `xlsx` and you want to compare it with the LMS copy (`csv` downloaded from BlackBoard), this codebase compares between those two files (`xlsx` and `csv`) to check if there are any mismatch with the `xlsx` file. It basically compares between two columns (students' marks) for each student ID.

It is assumed that some marks may be directly entered in the LMS; so, the codebase will only compare between the two files for the students who have marks in the `xlsx` file.

## Usage
Configure filenames and run:
```bash
./match_mark.sh
```
It will ask for `lms_col` and `local_col`. Alternatively, you can pass them as arguments:

```bash
python3 match.py --lms <lms_file.csv> --lms_col <LMS_COL> --local <local_file.xlsx> --local_col <LOCAL_COL>
```

The output will be sorted by last name.

## Arguments

```bash
  -h, --help          show this help message and exit
  --lms               Path to LMS csv file
  --lms_col           nth LMS column to compare with
  --local             Path to local xlsx file
  --local_col         nth Local column to compare with
```