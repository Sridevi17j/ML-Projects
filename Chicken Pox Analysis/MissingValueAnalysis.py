import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
import json

class clMissingValueAnalysis():

    def __init__(self,filepath):
        self.file1=filepath

    def fnMissingValueAnalysis(self):
        try:
            df = pd.read_csv(self.file1)
            df=df.T.drop_duplicates().T
            #df = df.drop('Date', axis=1)
            imputer = KNNImputer(n_neighbors=3, weights='uniform', missing_values=np.nan)
            print("missing value module is being processed")
            self.new_array = imputer.fit_transform(df)
            self.new_data = pd.DataFrame(data=self.new_array, columns=df.columns)
            return self.new_data
        except Exception as e:
            raise e



