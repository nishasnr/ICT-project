"""
app_data.py loads the data required, acts as the 'middleman' between other functions/files and all the application's data needs

Criteria Fulfilled:
-File operation and Exception handling (opening_data, food_data, stall_data)
-Use of Dictionary (stalls Dictionary)
-Use of tuple/list (days and stalls_list Tuple)
-Use of string operations/functions (Replacing the string $x.xx with float x.xx)
"""
import pandas as pd

# By Nisha and Kyaw
# Stalls and days of week tuples for easy referencing
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

# Immutable Tuple to store information
stalls_list = (
    "mcdonalds",
    "starbucks",
    "ljs",
    "pizzahut",
    "kfc",
    "subway",
    "miniwok",
    "ytf",
    "chickenrice",
    "handmade",
    "mixedrice",
    "western",
    "roastedduck",
    "hotbeverages",
    "soup",
    "malaybbq",
    "vegetarian",
    "indian",
    "salad",
    "mala",
    "bbq",
    "pasta",
    "viet",
    "jap",
    "xian")

# Dictionary for stalls short forms for easy referencing
# Useful since some stall names have special characters or spaces in them
# which can cause issues in the code if we just use them plainly
stalls = {
	"mcdonalds": "McDonald's",
	"starbucks":"Starbucks",
	"ljs":"Long John Silver's",
	"pizzahut": "Pizza Hut",
	"kfc": "KFC",
	"subway": "Subway",
	"miniwok": "Mini Wok",
	"ytf":"Yong Tau Foo",
	"chickenrice":"Chicken Rice",
	"handmade":"Handmade Noodles",
	"mixedrice":"Mixed Rice",
	"western":"Western",
	"roastedduck":"Cantonese Roast Duck",
	"hotbeverages": "Hot Beverages",
	"soup": "Soup Delight",
	"malaybbq": "Malay BBQ",
	"vegetarian": "Vegetarian Food",
	"indian": "Indian",
	"salad": "Salad",
	"mala": "Mala Hot Pot",
	"bbq": "BBQ Delight",
	"pasta": "Italian Pasta",
	"viet": "Vietnamese Cuisine",
	"jap": "Japanese Korean Delight",
	"xian": "Xi'an Mei Shi"}

# Loading in the data from a csv file
opening_data = pd.read_csv('data/openinghours.csv')
food_data = pd.read_csv('data/nsfood.csv')
stall_data = pd.read_csv('data/stallinfo.csv')

# Replacing the string $x.xx with float x.xx
food_data["Price"]=food_data["Price"].replace('[\$,]', '', regex=True).astype(float)
