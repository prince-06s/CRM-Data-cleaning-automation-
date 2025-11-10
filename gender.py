null_values = {
     "-", "--", "---", ".", "..", "...",
    "na", "n.a", "n/a", "n\\a", "n.a.", "n.a..",
    "null", "none", "Null", "None", "NULL",
     "not specified",
    "missing", "undisclosed",
    "unavailable", "not provided", "no info",
    "?", "??", "???", "🫥", "🤷", "🙅", "🤐"
}
gender_emoji_mapping = {
    # 👨 Male Emojis
    '👨': 'M',
    '👨🏻': 'M', '👨🏼': 'M', '👨🏽': 'M', '👨🏾': 'M', '👨🏿': 'M',
    '👦': 'M',
    '👨‍🦰': 'M', '👨‍🦱': 'M', '👨‍🦲': 'M', '👨‍🦳': 'M',
    '👨‍⚕': 'M', '👨‍🎓': 'M', '👨‍🏫': 'M', '👨‍⚖': 'M',
    '👨‍🌾': 'M', '👨‍🍳': 'M', '👨‍🔧': 'M', '👨‍🏭': 'M',
    '👨‍💼': 'M', '👨‍🔬': 'M', '👨‍💻': 'M', '👨‍🎤': 'M',
    '👨‍🎨': 'M', '👨‍✈': 'M', '👨‍🚀': 'M', '👨‍🚒': 'M',
    '🕵‍♂': 'M', '🧑‍🦰‍♂': 'M', '🧑‍🦱‍♂': 'M',
    '👩': 'F',
    '👩🏻': 'F', '👩🏼': 'F', '👩🏽': 'F', '👩🏾': 'F', '👩🏿': 'F',
    '👧': 'F',
    '👩‍🦰': 'F', '👩‍🦱': 'F', '👩‍🦲': 'F', '👩‍🦳': 'F',
    '👩‍⚕': 'F', '👩‍🎓': 'F', '👩‍🏫': 'F', '👩‍⚖': 'F',
    '👩‍🌾': 'F', '👩‍🍳': 'F', '👩‍🔧': 'F', '👩‍🏭': 'F',
    '👩‍💼': 'F', '👩‍🔬': 'F', '👩‍💻': 'F', '👩‍🎤': 'F',
    '👩‍🎨': 'F', '👩‍✈': 'F', '👩‍🚀': 'F', '👩‍🚒': 'F',
    '🕵‍♀': 'F', '🧑‍🦰‍♀': 'F', '🧑‍🦱‍♀': 'F',
    '🧑': 'O',
    '🧑🏻': 'O', '🧑🏼': 'O', '🧑🏽': 'O', '🧑🏾': 'O', '🧑🏿': 'O',
    '🧒': 'O',
    '🧑‍🦰': 'O', '🧑‍🦱': 'O', '🧑‍🦲': 'O', '🧑‍🦳': 'O',
    '🧑‍⚕': 'O', '🧑‍🎓': 'O', '🧑‍🏫': 'O', '🧑‍⚖': 'O',
    '🧑‍🌾': 'O', '🧑‍🍳': 'O', '🧑‍🔧': 'O', '🧑‍🏭': 'O',
    '🧑‍💼': 'O', '🧑‍🔬': 'O', '🧑‍💻': 'O', '🧑‍🎤': 'O',
    '🧑‍🎨': 'O', '🧑‍✈': 'O', '🧑‍🚀': 'O', '🧑‍🚒': 'O',
    '🧝': 'O', '🧚': 'O', '🧞': 'O', '🧛': 'O',
    '⚧': 'O',  # Transgender symbol
    '🚻': 'O',  # Gender-inclusive restroom
    '🏳‍⚧': 'O',  # Transgender pride flag
    '🏳‍🌈': 'O',  # LGBTQ+ flag
    "👨": "M", "🧔": "M", "👱‍♂": "M", "👨‍🦱": "M", "👨‍🦰": "M",
    "👨‍🦲": "M", "👨‍🦳": "M", "👨♂": "M", "♂": "M",
    "👩": "F", "👱‍♀": "F", "👩‍🦱": "F", "👩‍🦰": "F",
    "👩‍🦲": "F", "👩‍🦳": "F", "👩♀": "F", "♀": "F",
    "⚧": "O", "🏳‍⚧": "O", "🧑‍⚧": "O", "🧑": "O", "🧑‍🦱": "O",
    "🧑‍🦲": "O", "🧑‍🦳": "O", "🧑‍🦰": "O", "🧒": "O",
     "🚹": "M",
    "🚺": "F",
    "⚧": "O",
    "♂": "M",
    "♀": "F",
    "🏳‍⚧": "O",
    "🏳‍🌈": "O",
    "👨": "M", "👨🏻": "M", "👨🏼": "M", "👨🏽": "M", "👨🏾": "M", "👨🏿": "M",
    "👩": "F", "👩🏻": "F", "👩🏼": "F", "👩🏽": "F", "👩🏾": "F", "👩🏿": "F",
    "🧑": "O", "🧑🏻": "O", "🧑🏼": "O", "🧑🏽": "O", "🧑🏾": "O", "🧑🏿": "O",
    "👨‍🦰": "M", "👩‍🦰": "F",  # red hair
    "👨‍🦱": "M", "👩‍🦱": "F",  # curly hair
    "👨‍🦳": "M", "👩‍🦳": "F",  # white hair
    "👨‍🦲": "M", "👩‍🦲": "F",  # bald
    "👱‍♂": "M", "👱‍♀": "F",  # blonde hair
    "🕺": "M", "💃": "F",        # dancing
    "🧔": "M", "🧔🏻": "M", "🧔🏼": "M", "🧔🏽": "M", "🧔🏾": "M", "🧔🏿": "M",  # beard (mostly male)
    "🧕": "F", "🧕🏻": "F", "🧕🏼": "F", "🧕🏽": "F", "🧕🏾": "F", "🧕🏿": "F",  # hijab (female-coded)
}
gender_translation_dict = {
    "M": [
        "male", "man", "boy", "m", "masculine",
        "पुरुष", "लड़का",  # Hindi
        "男", "男性",       # Chinese
        "maschio",         # Italian
        "masculino",       # Spanish / Portuguese
        "männlich",        # German
        "мужчина",         # Russian
        "erkek",           # Turkish
        "hombre",          # Spanish
        "ชาย",             # Thai
        "남자",             # Korean
        "男性",             # Japanese
        "ชาย", "ผู้ชาย",     # Thai
        "purusha", "purush",  # Hindi/phonetic
        "مذكر",            # Arabic
        "mies",            # Finnish
        "mees",            # Estonian
        "férfi",           # Hungarian
        "bărbat",          # Romanian
        "vir",             # Latin
        "homme",           # French
        "mann",            # Norwegian / German
    ],
    "F": [
        "female", "woman", "girl", "f", "feminine",
        "महिला", "औरत", "लड़की",     # Hindi
        "女", "女性",                # Chinese / Japanese
        "femmina",                  # Italian
        "feminino",                 # Spanish / Portuguese
        "weiblich",                 # German
        "женщина",                  # Russian
        "kadın",                    # Turkish
        "mujer",                    # Spanish
        "หญิง", "ผู้หญิง",           # Thai
        "여자",                      # Korean
        "femme",                    # French
        "vrouw",                    # Dutch
        "féminin",                  # French
        "monyet betina",            # Indonesian (edge slang)
        "امرأة", "أنثى",             # Arabic
        "nainen",                   # Finnish
        "naine",                    # Estonian
        "nő",                       # Hungarian
        "femeie",                   # Romanian
        "femina",                   # Latin
        "kvinne",                   # Norwegian
    ],
    "O": [
        "other", "nonbinary", "non-binary", "transgender", "trans", "nb", "genderqueer", "fluid", "bigender", "pangender", "neutrois", "agender",
        "third gender", "no gender", "genderless", "unknown", "prefer not to say", "x", "none", "n/a", "na", "-",
        "अन्य", "पता नहीं",               # Hindi
        "其他", "未知",                     # Chinese
        "altro", "sconosciuto",            # Italian
        "otro", "desconocido",             # Spanish
        "anderes", "unbekannt",            # German
        "другое", "неизвестно",            # Russian
        "diğer", "bilinmiyor",             # Turkish
        "อื่น", "ไม่ทราบ",                  # Thai
        "기타", "모름",                     # Korean
        "その他", "不明",                    # Japanese
        "autre", "inconnu",                # French
        "anders",                          # Dutch
        "آخر", "غير معروف",                # Arabic
        "tuntematon",                      # Finnish
        "muud",                            # Estonian
        "más",                             # Hungarian
        "altul", "necunoscut",             # Romanian
        "alienus", "ignotus",              # Latin
    ]
}
gender_slang_mapping = {
    'M': [
        'male', 'm', 'man', 'boy', 'guy', 'dude', 'bro', 'gentleman', 'he', 'him',
        'bhai', 'bhaiya', 'ladka', 'purush', 'ชาย', '男', 'macho', 'herr', 'sir',
        'boi', 'gent', 'boyo', 'homie', 'chap', 'bruh', 'alpha male', 'yo bro'
    ],

    'F': [
        'female', 'f', 'woman', 'girl', 'lady', 'madam', 'she', 'her',
        'didi', 'behen', 'ladki', 'mahila', 'หญิง', '女', 'gal', 'miss', 'ms',
        'queen', 'chick', 'sis', 'girlie', 'lass', 'babe', 'bbygirl', 'diva','gurl'
    ],

    'O': [
        'nonbinary', 'non-binary', 'transgender', 'trans', 'genderfluid', 'gender queer', 'genderqueer',
        'agender', 'bigender', 'neutrois', 'third gender', 'nb', 'n.b.', 'they', 'them',
        'intersex', 'enby', 'pangender', 'two-spirit', 'hijra', 'kathoey', 'other', 'none',
        'different', 'fluid', 'xgender', 'gender non-conforming', 'gnc', 'mtf', 'ftm', 'mx'
    ]
}

gender_other_mapping = {
    "O": [
        "other", "o", "othr", "oth", "others", "otheer", "otthr",
        "nonbinary", "non binary", "non-binary", "nb", "enby",
        "genderqueer", "gender queer", "gq", "gendrqueer", "genderqeer",
        "genderfluid", "gender fluid", "gfluid", "genderflud",
        "transgender", "trans gender", "trans", "trnsgender", "trangender", "transgen",
        "transwoman", "trans woman", "transfemale", "trans female", "mtf",
        "transman", "trans man", "transmale", "trans male", "ftm",
        "agender", "a gender", "agen", "agendr",
        "bigender", "bi gender", "bigendr",
        "pangender", "pan gender", "pangendr",
        "androgynous", "androgyne", "androgyn",
        "two spirit", "two-spirit", "2spirit", "2 spirit", "2s",
        "third gender", "thirdgender", "3rdgender",
        "neutrois", "neutroisgender",
        "demiboy", "demi boy", "demiman", "demi man",
        "demigirl", "demi girl", "demiwoman", "demi woman",
        "intersex", "inter sex", "intresex", "intersx",
        "questioning", "quest", "gender questioning",
        "neither", "none", "no gender", "no-gender",
        "genderless", "gndrless", "gender neutral", "neutral gender",
        "unknown", "unk", "u", "unsp", "n/a", "n.a.", "prefer not to say",
        "🧑‍🦲", "⚧", "🌈", "🤷", "🧠", "🚻", "👤",  # symbols sometimes used in forms or UI
    ]
}

normal_mapping = {
    'male' : 'M',
    'female' : 'F',
    'other' : 'O'
}

leet_map = {
    '1' : 'l',
    '3' : 'e',
    '4' : 'a',
    '0' : 'o',
    '@' : 'a',
    '!' : 'i'
}

output = ['O','M','F']
manual_check = {}

import pandas as pd
import numpy as np
import unicodedata
from unidecode import unidecode
import ftfy
import re
from ftfy import fix_text
import rapidfuzz

from rapidfuzz import process


def clean_gender(value,idx):

  original = value



  def flag(idx,original):



    if not idx in manual_check:
      manual_check[idx] = original


  def main_cleaning(value,idx):

    

    if pd.isna(value):
      return np.nan

    if not isinstance(value,str):
      value = str(value)

    value = value.strip().lower()



    if pd.isna(value) or value.strip() == '' or value in null_values:
      return np.nan

    if value in gender_emoji_mapping:
      value = gender_emoji_mapping[value]

    flat_gender_map = {}

    for label , native_lang in gender_translation_dict.items():
      for native_word in native_lang:
        clean_native = native_word.lower().strip().replace(' ','')
        flat_gender_map[clean_native.strip()] = label

    if value in flat_gender_map:
      value = flat_gender_map[value]


    value = fix_text(value)
    value = unidecode(value).strip()
    value = unicodedata.normalize('NFKD',value)
    value = re.sub(r'[\u200b\u200c\u200d\u202e\u2060\u00a0]','',value)
    value = re.sub(r'\s+',' ',value)

    value = value.strip().lower()
    value = re.sub(r'[^a-zA-Z\s]+','',value)


    clean_value = []

    for char in value:
      if char in leet_map:
        char = leet_map[char]
        clean_value.append(char)

      else:
        clean_value.append(char)

    value = ''.join(clean_value)

    flat_gender_slang = {}
    for gender , variants in gender_slang_mapping.items():
      for slangs in variants:
        clean_slangs = slangs.lower().strip().replace(' ','')
        flat_gender_slang[clean_slangs.strip()] = gender

    if value in flat_gender_slang:
      value = flat_gender_slang[value]

    flat_other_slang = {}


    for corrects , slangs in gender_other_mapping.items():
      for thing in slangs:
        clean_thing = thing.lower().strip().replace(' ','')
        flat_other_slang[clean_thing] = corrects

    if value in flat_other_slang:
      value = flat_other_slang[value]



    choices = ['other','female','male']

    result = process.extractOne(value,choices,score_cutoff = 80)

    if result:
      match , score , _ = result
      value = match


    if value in normal_mapping:
      value = normal_mapping[value]




    value = re.sub(r'[^a-zA-Z\s]+','',value)


    if pd.isna(value):
      return np.nan




    return value.title()


  def validation(value,idx,original):


    if not isinstance(value,str):
      value = str(value)


    if pd.isna(value) or value in null_values or value.strip() == '':
      return np.nan


    if not value in output:
      flag(idx,original)


    if pd.isna(value):
      return value


    return value.title()


  cleaned = main_cleaning(value,idx)
  if pd.isna(cleaned):
    return np.nan

  validated = validation(cleaned,idx,original)
  if pd.isna(validated):
    return np.nan
  return validated




df['Gender'] = df.apply(lambda row : clean_gender(row['Gender'],row.name),axis = 1)
df = df.dropna(subset=['Gender'])

pd.set_option('display.max_rows',None)

for i,v in manual_check.items():
  print([i,v])
df