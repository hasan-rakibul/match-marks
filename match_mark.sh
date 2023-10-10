read -p "lms_col: " lms_col
read -p "local_col: " local_col

python match.py \
--lms gc_2023_2_COMP1002_V1_L1_A1_INT_772330_fullgc_2023-10-10-14-18-48.csv \
--lms_col $lms_col \
--local DSAmarking_Semester_2_2023.xlsx \
--local_col $local_col                                                                                                       