import happybase
import io, argparse

hostname = '127.0.0.1'
port = 9090
table_name = 'food_data'

parser = argparse.ArgumentParser()
parser.add_argument('-ho', '--host', action ='store', dest='host', default=hostname, help='master node host')
parser.add_argument('-po', '--port', action ='store', dest='port', default=port, help='master node port')
parser.add_argument('-tn', '--tablename', action ='store', dest='table_name', default=table_name, help='table name')

#parser.add_argument('-co', '--food_code', action ='store', dest='code',  help='Food_Code')
#parser.add_argument('-pr', '--portion_default', action ='store', dest='portion',  help='Portion_Default')
parser.add_argument('-dn', '--display_name', action ='store', dest='display_name', help='Display_Name')
args=parser.parse_args()

connection = happybase.Connection(host = args.host, port = args.port,  autoconnect=False)
connection.open()
table = connection.table(args.table_name)
rows = table.scan(filter="SingleColumnValueFilter ('data', 'Display_Name', =, 'binary:{d_n}')".format(d_n = args.display_name))

for key, data in rows:
    print(key, data)


connection.close()
