## To create a new table with a singl colum family:

### Copy populate_single.py and Food_Display_Table.xlsx to hbase-maser node:
```
docker cp <path>\populate_single.py <container id>:populate_single.py

docker cp <path>\Food_Display_Table.xlsx <container id>:Food_Display_Table.xlsx
 ```

### In hbase-master node cli run:
```
apt-get update

apt install python3-pandas

apt install python3-xlrd
```
### Now run the script:

```
python3 populate_single.py
```

### This will run single command for each cell of each row of data set and that takes ages. Ok, not ages, but hours - many of them.

## ___________________________________________________________________________


# But don't you worry - we have another script:
-   ### stop distributed hbase (in hbase repo):
     ```
    docker-compose -f docker-compose-distributed-local.yml down
    ```
-   ### delete image of master node via docker desktop end rerun 
-   ### add "- 9090:9090" after line 78 docker-compose-distributed-local.yml
-   ### run local distributed hbase again:
    ```
    docker-compose -f docker-compose-distributed-local.yml up -d
    ```
-   ### copy script to master node container
    ```
    docker cp <path>\populate_with_happybase.py <container id>:pwh.py

    ```
-   ### if you haven't copied Food_Display_Table.xlsx to hbase-maser node:

    ```
    docker cp <path>\Food_Display_Table.xlsx <container id>:Food_Display_Table.xlsx

    ```
-   ### open CLI of master node and run
    ```
    hbase thrift start
    ```
-   ### open yet another CLI of master node and run
    ```
    python pwh.py
    ```
    #### if you want to choose table name yourself run
    ```
    python pwh.py -tn 'your fancy table name'
    ```
### As we opened port 9090 in the container of master node, you can also run the script from your local machine. If your master node runs on different ports or host, you can specify that with
    ```
    python pwh.py -po <port number> -ho 'host name'
    ```
