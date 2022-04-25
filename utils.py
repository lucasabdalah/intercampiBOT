"""
Created on Mon Apr 25 13:17:13 2022
@author: lucasabdalah
"""
import pandas as pd

def get_data_sheet(googleSheetId, worksheetName):
  URL = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
	googleSheetId,
	worksheetName
)
  return pd.read_csv(URL)

data_sheet = get_data_sheet(googleSheetId = '1udCmyijNOsHivgMFmtcHrWMIqI2MliXv', worksheetName = 'P%C3%A1gina1')

data_sheet.head(10)