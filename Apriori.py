
import pandas as pd

from itertools import combinations

excel_file = "dba_1.xlsx"
database = pd.read_excel(excel_file, header=None)

#print(database)

#min_support = input('Enter Minimum Support Value')


#Gets all unique items 

unique_items = set()
for i, entry in database.iterrows():
    for item in entry:
        unique_items.add(item)

unique_items.remove(pd.np.nan)
print(unique_items)


#combinations of unique items
tables = []
for i in range(1,len(unique_items)):
    table = {}
    comb = list(combinations(unique_items, i))
    print(comb)
    for i, entry in database.iterrows():
        print(list(entry))
        input()
        
