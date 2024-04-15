read -p "lms_col: " lms_col
read -p "local_col: " local_col

python main.py \
--lms gc_2024_1_COMP1002_V1_L1_A1_INT_793226_fullgc_2024-04-15-19-29-34.csv \
--lms_col $lms_col \
--local "DSA marking_semester 1 2024.xlsx" \
--local_col $local_col                                                                                      