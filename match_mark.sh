read -p "lms_col: " lms_col
read -p "local_col: " local_col

python main.py \
--lms gc_2023_2_COMP1002_V1_L1_A1_INT_772330_fullgc_2023-10-17-14-25-41.csv \
--lms_col $lms_col \
--local DSAmarking_Semester_2_2023.xlsx \
--local_col $local_col \
--print_exception                                                                                             