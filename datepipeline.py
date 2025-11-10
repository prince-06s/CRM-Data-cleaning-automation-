import pandas as pd
import numpy as np
import re

df = pd.read_csv('dates_column2.csv', on_bad_lines = 'skip')


noise = ['logged on','as of','next week','today','yesterday','logged on:','logged on :']
manual_check = {}
null_date_values = [
    '', ' ', 'nan', 'NaN', 'None', 'none', 'null', 'NULL', 'n/a', 'N/A',
    'na', 'NA', '--', '-', 'n.a', 'n.a.', '.', '..',
    'not available', 'Not Available', 'notavailable',
    'not disclosed', 'Not Disclosed', 'notdisclosed',
    'unknown', 'Unknown', 'unkown', 'UNK', 'missing', 'Missing',
    'nil', 'Nil', 'nill', 'notmentioned', 'not mentioned',
    'Date not provided', 'pending', 'later', 'sometime', 'undefined'
]
month_map = {
    'january': '01', 'jan': '01',
    'february': '02', 'feb': '02',
    'march': '03', 'mar': '03',
    'april': '04', 'apr': '04',
    'may': '05',
    'june': '06', 'jun': '06',
    'july': '07', 'jul': '07',
    'august': '08', 'aug': '08',
    'september': '09', 'sep': '09', 'sept': '09',
    'october': '10', 'oct': '10',
    'november': '11', 'nov': '11',
    'december': '12', 'dec': '12'
}
ordinal_date_map = {
    '1st': '01', '2nd': '02', '3rd': '03', '4th': '04', '5th': '05',
    '6th': '06', '7th': '07', '8th': '08', '9th': '09', '10th': '10',
    '11th': '11', '12th': '12', '13th': '13', '14th': '14', '15th': '15',
    '16th': '16', '17th': '17', '18th': '18', '19th': '19', '20th': '20',
    '21st': '21', '22nd': '22', '23rd': '23', '24th': '24', '25th': '25',
    '26th': '26', '27th': '27', '28th': '28', '29th': '29', '30th': '30',
    '31st': '31'
}


def clean_date(value):

  if  not isinstance(value,str):
    value = str(value)

  value = value.strip().lower()
#  value = value.replace(' ','')




  if value in  null_date_values or pd.isna(value):
    return np.nan


  for n in noise:
    value = value.replace(n,'')


  value = re.sub(r'[.\-\+]','/',value)
  value = re.sub(r'\s+','/',value)

  for wrong , right in month_map.items():
    pattern = r'\b' + wrong + r'\b'

    value = re.sub(pattern,right,value)


  for wrong , right in ordinal_date_map.items():
    pattern = r'\b' + wrong + r'\b'
    value = re.sub(pattern,right,value)






  value = re.sub(r'[^0-9/]','',value)

  if value.strip() == '':
    return np.nan


  value = re.sub(r'/+','/',value)
  value = value.strip('/')



  return value



df['date'] = df['date'].apply(clean_date)







def manual_date_formatter(value):
    if not isinstance(value, str):
        value = str(value)

    value = value.strip().strip('/')       # Remove outer spaces and slashes
    parts = value.split('/')

    # Case: Full date with three parts
    if len(parts) == 3:
        year = ''
        month = ''
        day = ''

        # Try to identify year (typically has 4 digits)
        for part in parts:
            if len(part) == 4:
                year = part
                break

        if year:
            parts.remove(year)
        else:
            # fallback if no 4-digit year found
            year = parts[2]
            parts = parts[:2]

        # Decide which is month and day
        if int(parts[0]) <= 12:
            month = parts[0]
            day   = parts[1]
        else:
            day   = parts[0]
            month = parts[1]

        return f"{year.zfill(4)}/{month.zfill(2)}/{day.zfill(2)}"

    # Case: Month + Year or Year + Month
    elif len(parts) == 2:
        if len(parts[0]) == 4:
            # Format: YYYY/MM
            year  = parts[0]
            month = parts[1]
        else:
            # Format: MM/YYYY
            month = parts[0]
            year  = parts[1]

        return f"{year.zfill(4)}-{month.zfill(2)}"

    # Case: Only Year
    elif len(parts) == 1:
        if len(parts[0]) == 4:
            return f"{parts[0]}"

    # Fallback for anything else
    return np.nan


df = df.dropna(subset = ['date'])
df['date_cleaned'] = df['date'].apply(manual_date_formatter)
df = df.dropna(subset = ['date_cleaned'])
df['date_cleaned']

