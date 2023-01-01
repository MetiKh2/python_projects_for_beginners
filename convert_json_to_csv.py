import pandas as pd

df=pd.read_json('products.json')
df.to_csv('products.csv',index=None)


#json file
# {
#   "Product": {
#     "0": "Desktop Computer",
#     "1": "Tablet",
#     "2": "Printer",
#     "3": "Laptop"
#   },
#   "Price": { "0": 700, "1": 250, "2": 100, "3": 1200 }
# }
