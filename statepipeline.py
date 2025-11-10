import numpy as np
import re
import pandas as pd
from rapidfuzz import process

null_state_values = [
    '',                     # empty string
    ' ',                    # space
    'nan', 'na', 'n/a',
    'null',
    'none',
    'missing',
    'unknown',
    'not available',
    '--', '-', 'nil',
    'nill',
    'undefined',
    'state missing', 'no state', 'no data',
    '???', '...', 'na.', 'na-', 'n.a', 'n a',
    'no location', 'location not known'
]

state_short_forms = {
    'mh': 'maharashtra',
    'up': 'uttar pradesh',
    'tn': 'tamil nadu',
    'dl': 'delhi',
    'wb': 'west bengal',
    'gj': 'gujarat',
    'rj': 'rajasthan',
    'ka': 'karnataka',
    'mp': 'madhya pradesh',
    'ap': 'andhra pradesh',
    'ts': 'telangana',
    'pb': 'punjab',
    'hr': 'haryana',
    'br': 'bihar',
    'jk': 'jammu and kashmir',
    'uk': 'uttarakhand',
    'od': 'odisha',
    'ch': 'chandigarh',
    'ga': 'goa',
    'tr': 'tripura',
    'mn': 'manipur',
    'ml': 'meghalaya',
    'as': 'assam',
    'ar': 'arunachal pradesh',
    'nl': 'nagaland',
    'sk': 'sikkim',
    'mz': 'mizoram',
    'hp': 'himachal pradesh',
    'jh': 'jharkhand',
    'cg': 'chhattisgarh',
    'ld': 'lakshadweep',
    'py': 'puducherry',
    'an': 'andaman and nicobar islands',
    'dnhdd': 'dadra and nagar haveli and daman and diu'
}


indian_states = [
    'andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', 'chhattisgarh',
    'goa', 'gujarat', 'haryana', 'himachal pradesh', 'jharkhand',
    'karnataka', 'kerala', 'madhya pradesh', 'maharashtra', 'manipur',
    'meghalaya', 'mizoram', 'nagaland', 'odisha', 'punjab',
    'rajasthan', 'sikkim', 'tamil nadu', 'telangana', 'tripura',
    'uttar pradesh', 'uttarakhand', 'west bengal',
    'andaman and nicobar islands', 'chandigarh', 'dadra and nagar haveli and daman and diu',
    'delhi', 'jammu and kashmir', 'ladakh', 'lakshadweep', 'puducherry'
]
manual_check = []

def fuzzing(value):
  if not isinstance(value,str):
    value = str(value)

  value = value.lower().strip()

  if pd.isna(value) or value.strip() == '' or value in null_state_values:
    return np.nan

  match , score , _ = process.extractOne(value,indian_states)
  if score >= 80:
    return match

  else:
     manual_check.append(value)

  return value


def clean_state(value):

  if not isinstance(value,str):

    value = str(value)

  value = value.strip()
  value = value.lower()


  value = re.sub(r'[^a-zA-Z\s*]','',value)

  if value in null_state_values or  pd.isna(value):
    return np.nan


  if value.strip() == '':
    return np.nan
  
  
  if value not in indian_states:
    manual_check.append(value)



  return value


df['state'] = df['state'].str.lower()
df['state'] = df['state'].apply(clean_state)
df['state'] = df['state'].replace(state_short_forms)
df['state'] = df['state'].apply(fuzzing)
df['state'] = df['state'].str.title()

df = df.dropna(subset = ['state'])


print(manual_check)
df['state']