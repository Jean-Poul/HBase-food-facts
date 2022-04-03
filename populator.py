import pandas as pd

file = "Food_Display_Table.xlsx"
table_name = "food_one_family"
column_family = "data"

food_data = pd.read_excel(file)
#print(food_data.head())
count=0
# for index in food_data.index:
#     if count==10:
#         break
#     else:
#         print(food_data.iloc[[index]])
#         count+=1

    
#row = food_data.iloc[[5]]

#print(type(row))
# print(food_data["Factor"])
# food_data.iat[0,0]
# print()

from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)


columns = list(food_data)
for i in range(0,10):
    print(food_data.iloc[i]["Portion_Amount"])

print("Connectiong to hbase")

def put_row(row):

    txt = "put 'food_one_family', '{Food_Code}', 'data:{att}, '{value}', {ts}"
    

    for c in columns:
        if c!="Food_Code":
            
            if row[c]==0:
                print("Zero")
            else:
                out = txt.format(Food_Code = row['Food_Code'], att = c, value = row[c], ts = ts) 
                # print(c)
                # print(r[c])
                print(out)

r=food_data.iloc[5]
print(r)
print("_______________________________________________________________")

put_row(r)
