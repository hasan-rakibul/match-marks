# match-marks
Assuming you have a local copy of students' marks in `xlsx` and you want to compare it with the LMS copy (`csv` downloaded from BlackBoard), this codebase compares between those two files (`xlsx` and `csv`) to check if there are any mismatch with the `xlsx` file. It basically compares between two columns (students' marks) for each student ID.

It is assumed that some marks may be directly entered in the LMS; so, the codebase will only compare between the two files for the students who have marks in the `xlsx` file.

# Files
- `match_mark.sh` and `match.py`: Earlier version, which compares and outputs the result in the terminal.
- `main_update_lms.py`: Updated version
  - Compares and updates the LMS file based on local file
  - Reads mapping from `mapping.json` file, which must have correct mappings on what you want to compare. Remember they are numeric column numbers in corresponding CSV and XLSX files, and they start from 1.

## Usage
Configure mapping between the columns in the `xlsx` and `csv` files in the `mapping.json` file. Then run the following command:

```bash
python main_update_lms.py
```
