"""
   This piece of code appends a new column '#debates2020' to the csv file with
   with each row having a value equal to the number of times the hashtag '#debates2020'
   occurs in the Hashtags column of that row.

   The count is case-insensitive.
"""

import pandas as pd

# you can modify this as you wish
def processor(row, input):
   # count the number of times the input (substring) occurs in the Hashtags column of that row
   return str(row['Hashtags']).lower().count(input)


csv_input = pd.read_csv('sample.csv')


hashtag = "#debates2020"
csv_input[hashtag] = csv_input.apply(lambda row: processor(row, hashtag), axis=1)

csv_input.to_csv('output.csv', index=False)
