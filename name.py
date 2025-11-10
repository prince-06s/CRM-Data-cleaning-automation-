import pandas as pd
import numpy as np
import unicodedata
import re
from ftfy import fix_text
from unidecode import unidecode
import textstat
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

null_values = [
    'nan', 'na', 'n/a', 'n.a', 'n a', 'na.', 'na-', 'na_',
    'null', 'none', 'nil', 'nill',
    'undefined', 'unknown', 'unknwn', 'unavailable',
    'missing', 'missng', 'not available', 'not provided',
    'not applicable', 'not_applicable', 'not_app',
    '---', '--', '-', '', '_', '...', '??', '???',
    'no data', 'no info', 'no information', 'none given',
    'empty', 'blank', 'zero', 'nil value', 'n/a value'
]
char_mapping = set({
    '@',
    '$',
    '&',
    '!',
    '#',
    '*',
    '€',
    '¥',
    '¢',
    '£',
    '₹',
    '©',
    '®',
    '™'

})
titles_and_honorifics = set([
    # English + Common
    "mr", "mister",
    "mrs", "missus",
    "ms",
    "miss",
    "master",
    "mx", "mixter",

    # Academic / Professional
    "dr", "doctor",
    "prof", "professor",
    "phd", "doctor of philosophy",
    "mba", "master of business administration",
    "btech", "bachelor of technology",
    "mtech", "master of technology",
    "bsc", "bachelor of science",
    "msc", "master of science",
    "b.e", "bachelor of engineering",
    "m.e", "master of engineering",
    "md", "doctor of medicine",
    "dds", "doctor of dental surgery",
    "dmd", "doctor of medicine in dentistry",
    "do", "doctor of osteopathy",
    "rn", "registered nurse",
    "mbbs", "bachelor of medicine and bachelor of surgery",
    "dpharm", "diploma in pharmacy",
    "ms", "master of surgery",
    "dm", "doctorate of medicine",

    "ca", "chartered accountant",
    "cfa", "chartered financial analyst",
    "cs", "company secretary",
    "icwa", "cost and works accountant",
    "acs", "associate company secretary",

    # Spiritual / Religious / Cultural
    "baba", "guru", "sri", "shri", "shriman", "shrimati", "smt", "kumari",
    "saint", "swami", "father", "imam", "prophet",
    "bishop", "cardinal", "rabbi", "archbishop",

    # Royal / Formal
    "sir", "madam", "dame", "lord", "lady",

    # Military / Legal / Govt
    "er", "engineer",
    "adv", "advocate",
    "col", "colonel",
    "lt", "lieutenant",
    "capt", "captain",
    "major",
    "cmdr", "commander",
    "gen", "general",
    "sgt", "sergeant",
    "sub", "subedar",

    "pres", "president",
    "hon", "honourable",
    "min", "minister",
    "deputy",
    "justice",
    "comm", "commissioner",

    "ias", "indian administrative service",
    "ips", "indian police service",
    "irs", "indian revenue service",
    "ifs", "indian foreign service",
    "pcs", "provincial civil services",

    # Suffixes
    "jr", "junior",
    "sr", "senior",
    "ii", "iii", "iv",  # generational
    "retired", "rtd", "ex",

    # Misc
    "coach"
])
garbage_name_list = set([
    # Numbers
    "123", "000", "45678", "99999", "0000", "007", "420", "1010",
    # Alphanumeric junk
    "user123", "test456", "name007", "abc123", "xyz789", "abcde12345", "1a2b3c",
    # Keyboard smash
    "asdf", "qwerty", "zxcvbn", "lkjhg", "aaaa", "bbbb", "xxxx", "qqqqq", "xxx",
    # System/test/demo
    "test", "tester", "test1", "test user", "demo", "sample", "demo user",
    # Symbols
    "@name", "$name$", "%%", "", "###", "@@@@", "@user123", "#test", "!asd", "~name",
    # Emojis (unicode)
    "😎", "👑", "🧍‍♂", "🤖", "🚀", "💯", "🔥", "😂", "👍", "☠", "✌🏽", "😈", "🤑",
    # Null disguised
    "null", "none", "n/a", "na", "not available", "no name", "---", "_", "???", ".", "..",
    # Emails / phones / URLs
    "john@gmail.com", "9876543210", "name@yahoo.co.in", "https://", "www.name.com",
    # Too short
    "a", "b", "c", "d", "x", "y", "z",
    # Overly long
    "johnjohnjohnjohnjohnjohnjohnjohnjohnjohn", "aaaaaaaaaaaaaaaaaaaaaaa", "zzzzzzzzzzzzzzzzzzzzzz",
    # Code / hex
    "0x123ABC", "ABC123DEF", "ID001122", "USR_983", "emp_001",
    # Slang
    "dude", "bro", "girl", "boss", "hacker", "noob", "idiot", "champ", "guest",
    # Random words
    "admin", "manager", "employee", "staff", "company", "office", "data", "hello", "welcome"
])

drop_chars = set([
    '`', '~', '^', '*', '=', '<', '>', '\\', '/',
    '{', '}', '[', ']',   '"',  ':', ';',
    '•', '¤', '§', '¶', '×', '÷', '±', '∞', '≈', '≠',
    '“', '”', '‘', '’'
])
manual_check = {}

def clean_name(idx,value):


  def flag(idx,original,reason):
    if idx not in manual_check:
      manual_check[idx] = f"'{original}'|||'{reason}'"



  def main_cleaning(idx,value):


   # basic cleaning and fixing normal things



    if pd.isna(value) or value in null_values or value.strip() == '':
      return np.nan

    if not isinstance(value,str):
      value = str(value)

    original = value

    value = value.lower().strip()

    if pd.isna(value) or value in null_values or value.strip() == '':
      return np.nan

    # unicode junk cleaning logic
    value = fix_text(value)
    value = unidecode(value)
    value = unicodedata.normalize('NFKD' ,value)
    value = re.sub(r'[\u00A0\u2000-\u200B\u202F\u205F\u3000]',' ',value)
    value = re.sub(r'\s+',' ',value).strip()


    # logic for dropping certain character and do mapping on known and logical characters

    for char in drop_chars:
      value = value.replace(char,'')


  #  if any(char in value for char in char_mapping):
    # flag(idx,original,'special characters included')

    value = re.sub(r"[^a-z\s\-']",'',value)
    value = re.sub(r'-+','-',value)
    value = re.sub(r"'+","'",value)
    value = re.sub(r'\s+',' ',value).strip()


    value = str(value).strip().lower()
    words = value.split()

    cleaned_words = []

    for word in words:
      if not word.lower() in titles_and_honorifics:
        cleaned_words.append(word)


    value = ' '.join(cleaned_words)

    if value in garbage_name_list:
      flag(idx,original,'garbage value')





    return value


  def validation(idx,value,original):

    if not isinstance(value,str):
      value = str(value)

    value = value.lower().strip()

    if pd.isna(value) or value in null_values or value.strip() == '':
      return np.nan

    if not re.fullmatch(r"[a-z\s'-]+",str(value).strip()):
      flag(idx,original,'not proper format')


    if len(value) < 6 or len(value) > 50:
      flag(idx,original,'length problem')


    value = value.title()


    return value

  cleaned = main_cleaning(idx,value)
  if pd.isna(cleaned):
    return np.nan
  validated = validation(idx,cleaned,value)
  return validated



for idx , value in df['name'].items():
  df.at[idx,'name'] = clean_name(idx,value)

df = df.dropna(subset=['name'])



for i , v in manual_check.items():
  print([i,v])


pd.set_option("display.max_rows",None)
df.head(len(df))








