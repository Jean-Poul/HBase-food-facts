# Assignment 4 HBase Database for Food Nutrition Facts

## Group Members

- Allan Bo Simonsen, cph-as484
- Jean-Poul Leth-Møller, cph-jl360
- Magdalena Aleksandra Wawrzak, cph-mw216
- Nina Lisakowski, cph-nl163

## About This Project

This project will cover a simple python project to populate and read data from an HBase database.

The HBase is runned using a docker-compose setup from this repo:  
https://github.com/big-data-europe/docker-hbase

The data is based on this free public ressource from this link:  
https://catalog.data.gov/dataset/mypyramid-food-raw-data

See README_USE for instructions

## Deciding The Row Key
The dataset contains 26 columns and 2014 rows.  
When deciding row key, the most important aspect is that we create a unique value for each row.  
By looking at the dataset we see that food code is good candidate for our rowkey, except there is duplicate entries in this column.  
Therefore we have choosen to combine it with the column "Portion_Display_Name" to make each rowkey unique.  
That means our row key consist of column A "Food_Code" and column E "Portion_Display_Name" with the following syntax: "Food_Code:Portion_Display_Name"   
The rowkey creation can be seen in our code on [line 25](https://github.com/Jean-Poul/HBase-food-facts/blob/0b9743a1f0a5b061220a3c8a9cb93093d0ec7be7/populate_with_happybase.py#L25)

## Suggestions For Column Families
When suggesting column families it makes sense to group together column that have the same purpose or theme.  
Instead of having one column family for all columns we would suggest the following structure:  
| Column family name   |      Columns      |  Column names |  Explenation |
|----------|:-------------:|------:|------:|
| Identifier |  A & B | Food_Code, Display_Name |These are the primary way to identify the content of the row |
| Portion |    C, D & E   | Portion_default, Portion_Amount, Portion_Display_Name | These columns all have in common that they describe the portion of the food |
| Calculation | F, G & H |    Factor, Increment, Multiplier | These all have in common that they are used for some kind of calculation related to the portion|
| Ingredients | I - T |   Grains, Whole_Grain, Vegetables, Orange_Vegetable, Drkgreen_Vegetable, Starchy Vegetables, Other_Vegetable, Fruits, Milk, Meats, Soy, Drybeans_peas | These columns all have in common that they describe some kind of ingredient that the food item contains |
| Nutrition | U - Z | Oils, Solid_Fats, Added_Sugar, Alcohol, Calories, Saturated_Fats |These columns could all we used to describe the nutritional content of the food|

## How To Use
For instructions on how to run insert and search scripts see README_USE. The scripts are written in python.
