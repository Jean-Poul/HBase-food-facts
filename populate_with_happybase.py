from __future__ import unicode_literals
import happybase
import pandas as pd
import io, argparse
import sys
reload(sys)
sys.setdefaultencoding('utf8')

hostname = '127.0.0.1'
port = 9090
table_name = 'food_data'
file = "Food_Display_Table.xlsx"
column_family = "data"
food_data = pd.read_excel(file)

parser = argparse.ArgumentParser()
parser.add_argument('-ho', '--host', action ='store', dest='host', default=hostname, help='master node host')
parser.add_argument('-po', '--port', action ='store', dest='port', default=port, help='master node port')
parser.add_argument('-tn', '--tablename', action ='store', dest='table_name', default=table_name, help='table name')
args=parser.parse_args()

columns = list(food_data)

def put_row(row, b):
    key = '{Food_Code}:{Portion_Display_Name}'.format(Food_Code = row['Food_Code'], Portion_Display_Name = row['Portion_Display_Name']).decode('utf8').encode(encoding = 'UTF-8')
    attributes= {}
    for c in columns:
        if c!="Food_Code" and c!="Portion_Display_Name":            
            if row[c]!=0:
                att_name = "{cf}:{cn}".format(cf = column_family, cn = c).decode('utf8').encode(encoding = 'UTF-8')
                att_value=str(row[c]).decode('utf8').encode(encoding = 'UTF-8')
                #attributes[str.encode(att_name)] = str.encode(att_value)    
                attributes[att_name]=att_value    
    b.put(key, attributes)

def put_row(row, b):
    key = '{Food_Code}:{Portion_Display_Name}'.format(Food_Code = row['Food_Code'], Portion_Display_Name = row['Portion_Display_Name']).encode(encoding = 'UTF-8')
    attributes= {}
    for c in columns:
        if c!="Food_Code" and c!="Portion_Display_Name":            
            if row[c]!=0:
                att_name = "{cf}:{cn}".format(cf = column_family, cn = c).encode(encoding = 'UTF-8')
                att_value=str(row[c]).encode(encoding = 'UTF-8')
                #attributes[str.encode(att_name)] = str.encode(att_value)    
                attributes[att_name]=att_value    
    b.put(key, attributes)

connection = happybase.Connection(host = args.host, port = args.port,  autoconnect=False)
connection.open()

print(connection.tables())
connection.create_table(args.table_name, {'data':dict()})
print(connection.tables())

table = connection.table(args.table_name)
batch = table.batch()

with table.batch() as b:
    for i in food_data.index:       
        put_row(food_data.iloc[i], b)
    b.send()

table.scan()
connection.close()


