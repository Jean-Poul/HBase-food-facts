import subprocess
import pandas as pd
from datetime import datetime

file = "Food_Display_Table.xlsx"
table_name = "food_single"
column_family = "data"
food_data = pd.read_excel(file)
create_command = "create '{table_name}', '{data}'".format(table_name = table_name, data = column_family)
dt = datetime.now()
ts = datetime.timestamp(dt)
columns = list(food_data)
    
def exectueCmd(cmd):
    p1 = subprocess.Popen(['echo', cmd], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['hbase', 'shell'], stdin=p1.stdout,
                            stdout=subprocess.PIPE)
    p1.stdout.close()
    output = []
    line = p2.stdout.readline()
    while line:
        output.append(line.strip())
        line = p2.stdout.readline()
    p2.stdout.close()
    return output

def put_row(row):
    txt = "put 'food_single', '{Food_Code}:{Portion_Display_Name}', 'data:{att}', '{value}', {ts}"   
    
    for c in columns:
        if c!="Food_Code" and c!="Portion_Display_Name":            
            if row[c]!=0:
                out = txt.format(Food_Code = row['Food_Code'], Portion_Display_Name = row['Portion_Display_Name'], att = c, value = row[c], ts = ts) 
                exectueCmd(out)
                print(out)



print("Creating table...")
exectueCmd(create_command)
print("Table created")
print("Saving data:")

for i in food_data.index:
    put_row(food_data.iloc[i])
print("Table populeted succesfully.")

