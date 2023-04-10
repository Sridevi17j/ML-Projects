import pandas as pd
import csv


class PreProcessing:



    def __int__(self,file):
        file=self.file




    def columnswithvalueszero(self):

        """
                   Check for entire columns with 0- Makes no meaning and drop it

        """

        df=pd.read_csv(self.file)
        emp_lst = []
        df_totalcolumn=df.shape[1]
        for i in range(0, df_totalcolumn, 1):
            if (df[df.columns[i]] == df[df.columns[i]][0]).all():
                emp_lst.append(df.columns[i])
        df.drop(emp_lst, axis=1,inplace=True)



    def getDuplicateColumns(self):

        """
            Check for columns with same value for target variable and make it as one column

        """
        
        duplicateColumnNames = set()
        for x in range(df.shape[1]):
            col = df.iloc[:, x]
            for y in range(x + 1, df.shape[1]):
                otherCol = df.iloc[:, y]
                if col.equals(otherCol):
                    duplicateColumnNames.add(df.columns.values[y])
        duplicateColumnNames_new=list(duplicateColumnNames)
        duplicateColumnNames_new.pop(0)
        df.drop(duplicateColumnNames_new,axis=1,inplace=True)


    def deletecorrelatedvariables(self):

        """
        Finding Correlated independent variables and deleting the highly correlated variables,by keeping one

        """

        col_corr = set()
        corr_matrix = df.corr()
        for i in range(len(corr_matrix.columns)):
            for j in range(i):
                if abs(corr_matrix.iloc[i, j]) > 0.9:
                    colname = corr_matrix.columns[i]
                    col_corr.add(colname)
        col_corr_new=list(col_corr)
        col_corr_new.pop(0)
        df.drop(col_corr_new,axis=1,inplace=True)

    def dftocsc(self):

        """
        converting preprocessed dataframe into final csv which will the input for ML models

        """
        df.to_csv('CSV Files/inputforMLModels.csv')







