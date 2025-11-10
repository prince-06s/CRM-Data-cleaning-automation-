import pandas as  pd
import numpy as np
import re
df = df_original.copy()
code = '91'
manual_check = []
null_phone_values = [
    '',  # empty string
    ' ',  # space
    'nan', 'NaN', 'NAN',
    'na', 'NA', 'n/a', 'N/A',
    'null', 'NULL',
    'none', 'None',
    'missing', 'Missing',
    'unknown', 'Unknown',
    'not available', 'Not Available',
    '--', '-', 'nil', 'Nil'
]

fake_phone_patterns = [
    '0000000000', '1111111111', '2222222222',
    '3333333333', '4444444444', '5555555555',
    '6666666666', '7777777777', '8888888888',
    '9999999999',

    '1234567890', '0123456789', '9876543210',
    '99999999999', '12345678901', '000000000000',

    # Landline lookalikes or repeated junk
    '1800123456', '1860123456',
    '999999', '1231231234', '0001112222',
]
india_variants = {
    'india', 'INDIA', 'India', 'IN', 'in', 'In',
    'IND', 'ind', 'Ind',
    '🇮🇳',  # emoji
    'bharat', 'Bharat', 'BHARAT',
    'india 🇮🇳', 'in 🇮🇳', 'IND 🇮🇳',
    'INDIA (IN)', 'IN - India', 'IN/India'
}


def clean_phone(value):

  if  not isinstance(value,str):
    value = str(value)

  flag = 0

  value = value.lower().strip()
  value = value.replace(' ','')


  for variant in india_variants :
    if variant in value:
      value = value.replace(variant,'91')


  value = re.sub(r'[^0-9]','',value)
  value = value.lstrip('0')


  if value.strip() == '':
    return np.nan

  if value in null_phone_values:
    return np.nan

 

  if value in fake_phone_patterns :
    flag = 1
    manual_check.append(value)


  if value.startswith(code):
    after_code = value[len(code):]
    if after_code.startswith('0'):
      after_code = after_code[1:]
    elif after_code.startswith('00'):
      after_code = after_code[2:]


    value = code + after_code


  if not value.startswith(code):
    value = code + value


  if len(value) != 12:
    flag = 1
    manual_check.append(value)


  value = '+' + value
  




  return (value,flag)


df = df.drop_duplicates(subset = ['phone'])
df = df.copy()

df[['phone','flag']] = df['phone'].apply(lambda x : pd.Series(clean_phone(x)))
df['flag'] = df['flag'].fillna(1).astype(int)



df = df.dropna(subset = ['phone'])


print('manual check')
for i in manual_check:
  print([i])
df