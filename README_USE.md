## To create a new table with a singl colum family:

### copy populate_single.py and Food_Display_Table.xlsx to hbase-maser node:

##### docker cp .\populate_single.py <container id>:populate_single.py

##### docker cp .\Food_Display_Table.xlsx <container id>:Food_Display_Table.xlsx

### in hbase-master node cli run:

##### apt-get update

##### apt install python3-pandas

##### apt install python3-xlrd

### now run the script:

##### python3 populate_single.py

### Tis will run single command for each cell of each row of data set and that takes ages. Ok, not ages, but hours - many of them.
