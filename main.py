import requests as rq
import pandas as pd
import sqlalchemy as sq
from sqlalchemy import create_engine
from variables import server_name, database_name

url = "https://dogapi.dog/api/v2/breeds?page%5Bnumber%5D=1&page%5Bsize%5D=20"


response = rq.get(url)
# print(response.status_code)
# print(response.json())

json = response.json()
df = pd.json_normalize(json,'data')

# print(df)
# path = r'F:\python_automation_projects\api_to_SQL\responseData.csv'
# df.to_csv(path,index=False)

# Connecting to MS-SQL server using windows authentication(No password required):
# If you use SQL authentication you will require password 
engine = create_engine(
    f"mssql+pyodbc://@{server_name}/{database_name}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Creating table in the created database:
df.to_sql(name='Dog_Breed',con=engine,index=False,if_exists='fail') # fail/replace/append : We have 3 options

# Its working
# Just remeber to put everything into specific functions. create a main function and call all the created functions 
# one by one serially inside the main function. Then do the if __name__="__main__": main() --> Industrial level refactoring
# Also you can put all the variables in a separate config file and import them while using. You can use a separate
# config supporting python library to do that.






