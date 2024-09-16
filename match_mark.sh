read -p "lms_col: " lms_col
read -p "local_col: " local_col

python main.py \
--lms lms.csv \
--lms_col $lms_col \
--local "local.xlsx" \
--local_col $local_col                                                                                      