import numpy as np
import pandas as pd
cal_hou_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv",sep = ",")
cal_hou_dataframe.describe()
cal_hou_dataframe.head()
cal_hou_dataframe.hist('housing_median_age')
cal_hou_dataframe.hist('longitude')
cal_hou_dataframe.hist('latitude')
hou=pd.DataFrame({'longitude':cal_hou_dataframe.longitude,'latitude':cal_hou_dataframe.latitude})
print(type(hou['longitude']))
print(hou['longitude'])
np.log(cal_hou_dataframe.longitude)