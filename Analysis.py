import pandas as pd
import numpy as np

train_value = pd.read_csv("Data/train_value.csv")
test = pd.read_csv("Data/test.csv")

column_labels = list(train_value.columns.values)
column_labels.remove("id")
column_labels.remove("amount_tsh")
column_labels.remove("date_recorded")
column_labels.remove("gps_height")
column_labels.remove("longitude")
column_labels.remove("latitude")
column_labels.remove("num_private")
column_labels.remove("region_code")
column_labels.remove("district_code")
column_labels.remove("population")
column_labels.remove("construction_year")

print(column_labels)
for i in column_labels:
	unique_value = list(set(np.concatenate((train_value[i].unique() , test[i].unique()))))
	print(len(unique_value))