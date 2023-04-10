import os.path

import pandas as pd
import numpy as np
from MissingValueAnalysis import clMissingValueAnalysis
import json
from sklearn.impute import KNNImputer
from dboperations import DBOperations

class prediction:

    def __init__(self,filepath):
        self.file1 = filepath

    def fnprediction(self):
        try:
            missing_obj=clMissingValueAnalysis(self.file1)
            outputoffnprediction=missing_obj.fnMissingValueAnalysis()
            DBObj=DBOperations()
            DBObj.insertdataintotable()
            DBObj.tabledatatocsv()
            preprocessingobj=PreProcessing('CSV Files/input.csv')
            preprocessingobj.columnswithvalueszero()
            preprocessingobj.getDuplicateColumns()
            preprocessingobj.deletecorrelatedvariables()
            preprocessingobj.dftocsc()
            return outputoffnprediction.head().to_json(orient='records')

        except Exception as e:
            raise e

        """   
        df=pd.read_csv(self.file1)
        df=df.drop('Date',axis=1)
        imputer = KNNImputer(n_neighbors=3, weights='uniform', missing_values=np.nan)
        print("missing value module is being processed")
        self.new_array = imputer.fit_transform(df)
        self.new_data = pd.DataFrame(data=self.new_array, columns=df.columns)
        return self.new_data.head().to_json(orient='records')
        """

        """
        obj_missingvalueanalysis = clMissingValueAnalysis(self.file1)
                self.file1=obj_missingvalueanalysis.fnMissingValueAnalysis()
                return self.file1.head().to_json(orient="records")
        """