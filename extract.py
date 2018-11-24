import numpy as np
import pandas as pd

cols = [0,1,5,6,7,8,117]
df = pd.read_csv('LANGEVIN_DATA.txt',delimiter=' ',usecols = cols, names = ['Time', 'Occupant Number', 'INDOOR Ambient Temp.', 'INDOOR Relative Humidity', 'INDOOR Air Velocity', 'INDOOR Mean Radiant Temp.', 'Predicted Mean Vote'])

def createCSV():
    df.to_csv('processed_data.csv',index = False)

if __name__ == '__main__':
    createCSV()
