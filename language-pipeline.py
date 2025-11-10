import pandas as pd
import numpy as np 
import re 
import unicodedata
from rapidfuzz import process , fuzz 

manual_check = set({})

language_labels = [
    'english', 'hindi', 'bengali', 'telugu', 'marathi', 'tamil', 'urdu', 'gujarati',
    'kannada', 'malayalam', 'punjabi', 'oriya', 'assamese', 'nepali', 'sanskrit',
    'sindhi', 'kashmiri', 'konkani', 'manipuri', 'bodo', 'santali', 'dogri', 'maithili',
    'french', 'german', 'spanish', 'portuguese', 'italian', 'russian', 'chinese',
    'japanese', 'korean', 'thai', 'vietnamese', 'burmese', 'arabic', 'turkish',
    'persian', 'pashto', 'hebrew', 'swahili', 'zulu', 'afrikaans', 'indonesian',
    'malay', 'filipino', 'mongolian', 'tibetan', 'greek', 'romanian'
]
language_mapping = {
    # English variants
    'english': 'english', 'eng': 'english', 'en': 'english', 'अंग्रेज़ी': 'english',

    # Hindi
    'hindi': 'hindi', 'हिन्दी': 'hindi', 'हिंदी': 'hindi', 'hin': 'hindi', 'hi': 'hindi',

    # Spanish
    'espanol': 'spanish', 'español': 'spanish', 'es': 'spanish', 'spanish': 'spanish',

    # French
    'francais': 'french', 'français': 'french', 'french': 'french', 'fr': 'french',

    # German
    'deutsch': 'german', 'german': 'german', 'de': 'german',

    # Chinese
    'chinese': 'chinese', 'zh': 'chinese', '中文': 'chinese', '汉语': 'chinese',

    # Arabic
    'arabic': 'arabic', 'عربى': 'arabic', 'ar': 'arabic',

    # Bengali
    'bengali': 'bengali', 'bangla': 'bengali', 'bn': 'bengali', 'বাংলা': 'bengali',

    # Gujarati
    'gujarati': 'gujarati', 'ગુજરાતી': 'gujarati', 'guj': 'gujarati', 'gu': 'gujarati',

    # Tamil
    'tamil': 'tamil', 'தமிழ்': 'tamil', 'ta': 'tamil',

    # Telugu
    'telugu': 'telugu', 'తెలుగు': 'telugu', 'te': 'telugu',

    # Kannada
    'kannada': 'kannada', 'ಕನ್ನಡ': 'kannada', 'kn': 'kannada',

    # Marathi
    'marathi': 'marathi', 'मराठी': 'marathi', 'mr': 'marathi',

    # Urdu
    'urdu': 'urdu', 'اردو': 'urdu', 'ur': 'urdu',

    # Punjabi
    'punjabi': 'punjabi', 'ਪੰਜਾਬੀ': 'punjabi', 'pa': 'punjabi',

    # Malayalam
    'malayalam': 'malayalam', 'മലയാളം': 'malayalam', 'ml': 'malayalam',

    # Korean
    'korean': 'korean', 'ko': 'korean', '한국어': 'korean',

    # Japanese
    'japanese': 'japanese', 'jp': 'japanese', 'ja': 'japanese', '日本語': 'japanese',
}



null_values = [
                                   # Empty / blank

    # Standard null indicators
    'na', 'n/a', 'n a', 'n.a', 'na.', 'na-',     # Not available variations
    'none', 'None',                              # Pythonic nulls
    'null', 'NULL',                              # API/database style
    'nan', 'NaN', 'NAN',                         # Numpy/pandas
     '---',                            # Dashes
    'nil', 'Nil', 'nill', 'NILL',                # Alternative words

    # Typos and junk
    'n0ne', 'nonne', 'nun',                      # Mistyped nulls
    'missng', 'misng', 'noen',                   # Typo variations
                               # Misused numeric                  # Confusion marks                         # Placeholder junk
    'undefined', 'Undefined',                    # JS or UI sources

    # Descriptive phrases
    'not available', 'Not Available',
    'not applicable', 'Not Applicable',
    'not provided', 'Not Provided',
    'no data', 'No Data',
    'no response', 'No Response',
    'not mentioned', 'Not Mentioned',
    'unavailable', 'Unavailable',
    'data missing', 'Data Missing',
    'missing', 'Missing',

    # AI, OCR, user error type entries
    'unkown', 'unknwon', 'unown',                # Typos of "unknown"
    'unknown', 'Unknown', 'UNKNOWN',             # Correct "unknown"
    'u/k', 'u.n.k.',                             # Abbreviated
    'unspecified', 'Unspecified',
    'n.a.', 'n.a', 'n - a',                      # Format abuse
    '[null]', '(null)', '{null}',               # Bracketed noise

    '###', 'xxxxx', 'xxxx',        # Masked or broken
    'field empty', 'value missing',              # Verbose
    'no answer', 'left blank',                   # Survey-type data
    'empty', 'EMPTY','other','others','otherlanguage','other language' ,'valuemissing',
                                   'datamissing','noanswer','leftblank','notmentioned','no mention'                # Literal
]



def clean_language(value):


  def basic_clean(value):
    if not isinstance(value,str):
      value = str(value)

    value = value.strip().lower()
    value = value.replace(' ','')
    value = re.sub(r'[^\w\s\u0900-\uFFFF]', '', value)
    value = unicodedata.normalize('NFKD',value).encode('ASCII','ignore').decode('utf-8')


    if value in null_values or value.strip() == '' or pd.isna(value):
      return np.nan

    
    return value

   

  
  def mapping_fuzzing(value):

    if value in language_mapping:
      return language_mapping[value]

    

    result = process.extractOne(value,language_labels,scorer= fuzz.ratio)
    if result is None:
      manual_check.add(value)
      return np.nan


    match , score, _ = result
    if score >= 85 :
      return match

    else:
      manual_check.add(value)
      return np.nan


  def validate(value):
    if pd.isna(value):
      return np.nan

    if value not in language_labels:
      manual_check.add(value)
      return np.nan

    return value



  cleaned = basic_clean(value)
  mapped = mapping_fuzzing(cleaned)
  validated = validate(mapped)
  return validated

    

df['Language'] = df['Language'].apply(clean_language)
df = df.dropna(subset = ['Language'])
df['Language'] = df['Language'].str.title()
df['Language']
for i in manual_check:
  print([i])
df['Language']