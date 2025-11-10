

manual_check = set()
word_digit_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
null_values = [
    '', ' ',                                # Empty or whitespace
    'nan', 'NaN', 'NAN',                    # NaN variations
    'na', 'NA', 'n/a', 'N/A',               # Not available formats
    'null', 'NULL',                         # Explicit nulls
    'none', 'None',                         # Python/JSON-style nulls
    'missing', 'Missing',                   # Informative missing
    'not available', 'Not Available',       # Long form
    '--', '-',                              # Dash formats
    'nil', 'Nil', 'nill', 'NILL',           # Alternate null words
    'undefined', 'Undefined',               # JS-style or APIs
    '?', '???', '...',                      # Confusion markers
    'na.', 'na-', 'n.a', 'n a',             # Alternate spacing/formatting
    'no data', 'not provided', 'not applicable', 'unavailable', 'unknown','hello' # Descriptive
]
def clean_pincode(value):


  def basic_clean(value):
      if not isinstance(value,str):
        value = str(value)

      value = value.strip().lower()

      if value in null_values or value.strip() == '' or pd.isna(value):
        return np.nan


      return value


  def clean_other(value):

    if pd.isna(value):
      return np.nan

    if not isinstance(value,str):
      value = str(value)

    value = re.sub(r'[^0-9a-zA-Z\s]','',value)

    if value in null_values or value.strip() == '' or pd.isna(value):
        return np.nan


    tokens = value.split()
    converted = ''

    try :

     converted = str(w2n.word_to_num(value))
     value = converted

    except :


      for token in tokens:
        if token in word_digit_map:
          converted = converted + word_digit_map[token]

        elif token.isdigit():
          converted += token

      if converted  :
        value = converted





    if len(value) != 6:
      return np.nan


    if value not in df_pincodes:
      return np.nan


    return value



  cleaned = basic_clean(value)
  if pd.isna(cleaned):
    return np.nan
  other = clean_other(cleaned)
  return other




df_pincodes = set(df_pincodes['pincode'].astype(str))
df['pincode'] = df['pincode'].apply(clean_pincode)
df = df.dropna(subset = ['pincode'])


def validation(value):
  return isinstance(value,str) and value.isdigit() and len(value) == 6

df['clean'] = df['pincode'].apply(validation)
df['pincode']