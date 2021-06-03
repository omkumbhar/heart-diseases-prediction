import pandas as pd

import sklearn.metrics as sm
from sklearn import tree

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



class Prediction :

    RF_tree = None

    def __init__(self):
        self.chd_data = pd.read_csv("./dataset/framingham1.csv")
        # self.printData()
        self.prepossesing()
        

    def printData(self):
        print(self.chd_data)

    def prepossesing(self):
        self.chd_data.dropna(subset=['education','cigsPerDay','BPMeds','glucose','BMI','totChol','heartRate'], inplace=True)


    def split_dataset(self):
        x = self.chd_data.drop(['TenYearCHD','BPMeds','heartRate','diabetes','totChol','diaBP'], axis = 1).values
        y = self.chd_data['TenYearCHD'].values
        return x,y

    def fitModel(self):
        x,y = self.split_dataset()
        RF_tree = RandomForestClassifier( criterion = 'entropy')
        RF_tree.fit(x, y)
        self.RF_tree = RF_tree
        


    # def printmat(self,x, y):
    #     print(  self.RF_tree.score(x, y) )

    def predict(self, x  ):
        return  self.RF_tree.predict([x])  






p = Prediction()
p.fitModel()
p.predict([  0,46,2,1,20,0,0,112,23.38,89    ])


print( f'predict = {p.predict([  0,46,2,1,20,0,0,112,23.38,89    ])}' )
print( f'predict = {p.predict([  1,30,2,0,0,0,1,120,23,70    ])}' )





# p.printmat()
# print(chd_data)  
# 0,46,2,1,20,0,0,112,23.38,89 


#     0,46,2,1,20,0,0,112,23.38,89    {1}