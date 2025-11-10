import pandas as pd
import numpy as np
import unicodedata
import ftfy
import re
import emoji
from rapidfuzz import process , fuzz
import tldextract

manual_check_imperfect = {}
manual_check_starting_problem = {}
manual_check_ending_problem = {}
null_values = set([
    "", None, np.nan, pd.NA,
    "null", "none", "nan", "na", "n/a", "not available", "not applicable",
    "missing", "unknown", "undisclosed", "unavailable", "no data",
    "empty", "not provided", "not given", "not entered",
    "prefer not to say", "invalid", "no value", "---", "xxx",
    "n a", "n\\a", "n.a", "n-a", "n.a.", "noone", "nul", "nnull", "na na",
    "nana", "n0ne", "nu11", "nil", "noemail", "no-email", "none given",
    "notentered", "no entry", "non", "na/na",
    "???", "###", "xxx@xxx.com", "test@test.com", "abc@abc.com",
    "fake@fake.com", "placeholder@email.com", "email@email.com",
    "email@domain.com", "user@domain.com", "123@123.com",
    "your@email.com", "example@example.com",
    "ＮＡ", "Ｎ／Ａ", "ｎｕｌｌ", "🅽🅰", "🆇🅇🆇", "🚫", "❌", "🈚"
])
email_tld_list = [
    # Common TLDs
    ".com", ".org", ".net", ".edu", ".gov", ".mil", ".int", ".info", ".biz", ".name", ".co",

    # Country Code TLDs (ccTLDs)
    ".in", ".uk", ".ca", ".au", ".de", ".fr", ".jp", ".cn", ".ru", ".br", ".za", ".it", ".nl",
    ".mx", ".kr", ".es", ".ae", ".sg", ".us", ".nz", ".ch", ".se", ".be", ".no", ".dk", ".fi",
    ".pl", ".gr", ".pt", ".tr", ".hk", ".id", ".ie", ".my", ".ar", ".vn", ".ro", ".th", ".sk",

    # Modern gTLDs
    ".ai", ".app", ".dev", ".tech", ".xyz", ".online", ".store", ".site", ".me", ".cloud",
    ".space", ".blog", ".digital", ".agency", ".design", ".tools", ".studio", ".media",
    ".services", ".world", ".group", ".today", ".company", ".news", ".life", ".systems",


]
trusted_domains = [
    "gmail", "yahoo", "outlook", "hotmail", "aol", "icloud", "protonmail",
    "zoho", "gmx", "yandex", "mail", "rediffmail", "msn", "live",
    "inbox", "rocketmail", "fastmail", "me", "qq", "163", "126",
    "india", "tutanota", "lycos", "comcast", "verizon", "sbcglobal",
    "btinternet", "bellsouth", "earthlink", "cox", "shaw", "charter",
    "att", "ymail", "hushmail", "pm", "mail2world", "naver", "sina",
    "zoznam", "seznam", "web", "telus", "ntlworld", "blueyonder",
    "optonline", "wanadoo", "orange", "virgin", "sky", "btopenworld",
    "peoplepc", "excite", "bigpond", "email", "myway", "usa",
    "netzero", "juno", "mailinator", "tiscali", "freemail", "laposte",
    "terra", "rambler", "eircom", "libero", "neuf", "onmail"
]

def clean_email(idx,value):

  original = value

  def flag_i(idx,original,reason):

    if not idx in manual_check_imperfect:
      manual_check_imperfect[idx] = f"{original}_____{reason}"


  def flag_s(idx,original,reason):
    if not idx in manual_check_starting_problem:
      manual_check_starting_problem[idx] = f"{original}_____{reason}"

  def flag_l(idx,original,reason):
    if not idx in manual_check_ending_problem:
      manual_check_ending_problem[idx] = f"{original}_____{reason}"


  def basic_cleaning(idx,value):

    if not isinstance(value,str):
      value = str(value)

    value = value.lower().strip()

    if pd.isna(value) or value in null_values or value.strip() == '':
      return np.nan


    value = ftfy.fix_text(value)
    value = emoji.replace_emoji(value,replace='')



    value = re.sub(r'[\u200b\u200c\u200d\u202a-\u202e\ufeff\xa0]','',value)
    value = value.strip().lower()
    value = value.strip('.,;:-_')
    value = re.sub(r'\s+','',value)
    value = re.sub(r'\s*@\s*','@',value)
    value = re.sub(r'\s*\.\s*','.',value)
    value = re.sub(r'\.{2,}','.',value)
    value = value.strip('"\'“”‘’')
    value = value.strip().lower()

    value = value.replace('[at]','@').replace('(at)','@')
    value = value.replace('[dot]','.').replace('(dot)','.')
    value = re.sub(r'\b(c0m|con|comm|coom|cm|ccom|coomm|c00m|c00mm|cc00mm)\b','com',value)



    return value

  def partial_cleaning(idx,value):

    if not isinstance(value,str):
      value = str(value)

    if pd.isna(value) or value in null_values or value.strip() == '':
      return np.nan

    value = value.lower().strip()

    if '@' not in value or '.' not in value:
      flag_i(idx,original,'not having @ or .')
      return 'manual_check'


    value = re.sub(r'\.{2,}','.',value)


    value = re.sub(r'^[^0-9a-zA-Z]+','',value)


    if not re.match(r'^[0-9a-zA-Z]',value):
      flag_s(idx,original,'invalid start')
      return 'manual_check'




    tld_store = re.search(r'\.([a-z]{2,10}(?:\.[a-z]{2,10})?)$',value.lower())

    if tld_store:
      tld = '.'+tld_store.group(1)

      result = process.extractOne(tld,email_tld_list,score_cutoff=90)

      if result:
        correct_tld , score , _ = result
        correct_tld = '.' + correct_tld.lstrip('.')
        value = re.sub(r'\.([a-z]{2,10}(?:\.[a-z]{2,10})?)$',correct_tld,value)





    pattern0 = r'(' + '|'.join(email_tld_list) + r')$'

    if not re.search(pattern0,value,re.IGNORECASE):
      flag_l(idx,original,'invalid ending')
      return 'manual_check'

    return value



  def main_cleaning(idx,value):

    if not isinstance(value,str):
      value = str(value)

    if pd.isna(value) or value.strip() == '' or value in null_values:
      return np.nan

    value = value.strip().lower()

    value = re.sub(r'@{2,10}','@',value)

    if not '@' in value or '.' not in value or value.count('@') != 1:
      flag_i(idx,original,'not having @ or .')
      return 'manual_check'



    if value.startswith('@') or value.endswith('@'):
      flag_i(idx,original,'@ problem')
      return 'manual_check'

    if '@' in value and value.count('@') == 1:
      global  local , domain = value.split('@')

      value = re.sub(r'\.{2,10}','.',value)

      if not re.search(r'[A-Za-z0-9!#$%&\'*+/=?^_`{|}~-]$', local):
        flag_i(idx,original,'local ending problem')
        return 'manual_check'

    else:
      flag_i(idx,original,'@ problem')
      return value


    extracted = tldextract.extract(domain)
    domain_name = extracted.domain
    suffix = extracted.suffix

    if not domain_name or not suffix:
      flag_i(idx,original,'imperfect')
      return 'manual_check'


    best_match , score , _ = process.extractOne(domain_name,trusted_domains,scorer=fuzz.ratio)

    if score >=80:
      corrected_domain = f"{best_match}.{suffix}"


      value = f"{local}@{corrected_domain}"


    else:
      flag_i(idx,original,'imperfect value')
      return f"{local}@{domain}"





    value = re.sub(r'[\u200b\u200c\u200d\u202a-\u202e\ufeff\xa0]', '', value)


    return value


  def validation(idx,value):

    if not isinstance(value,str):
      value = str(value)

    if pd.isna(value) or value.strip() == '' or value in null_values:
      return np.nan

    value =  value.strip().lower()
    pattern0 = r'(' + '|'.join(email_tld_list) + r')$'


    if not re.match(r'^[0-9a-zA-Z]',value):
      flag_s(idx,original,'invalid start')
      return 'manual_check'



    if not '@' in value or '.' not in value or value.count('@') != 1:
      flag_i(idx,original,'not having @ or .')
      return 'manual_check'

    if not re.search(pattern0,value,re.IGNORECASE):
      flag_l(idx,original,'invalid ending')
      return 'manual_check'


    format = f"{local}@{domain}"


    return value





  cleaned = basic_cleaning(idx,value)
  if pd.isna(cleaned):
    return np.nan

  partial = partial_cleaning(idx,cleaned)
  if pd.isna(partial):
    return np.nan

  main = main_cleaning(idx,partial)
  if pd.isna(main):
    return np.nan

  validated = validation(idx,main)
  return validated








df['email'] = df.apply(lambda row : clean_email(row.name,row['email']),axis=1)
df = df.dropna(subset=['email'])

for i,v in manual_check_imperfect.items():
  print([i,v])

for a,b in manual_check_starting_problem.items():
  print([a,b])

for a , b in manual_check_ending_problem.items():
  print([a,b])
df['email']

