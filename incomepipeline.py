import pandas as pd
import numpy as np
import re
from word2number import w2n

df = pd.read_csv('income_column1.csv')
df['df_original'] = df['income'].copy()

manual_review = []

lakh_variants = ['lakh', 'lakhs', 'lac', 'lacs', 'l', 'L']
currency_prefixes = [
    '₹', 'inr', '$', 'usd', '€', 'eur', '£', 'gbp',
    'rs', 'cad', 'aud', 'yen', 'jpy'
]

def cleaning_inconsistent(value):
    pattern = r'(\d+\.?\d*)\s*(' + '|'.join(lakh_variants) + r')\b'
    def repl(match):
        number = float(match.group(1))
        return str(int(number * 100000))
    return re.sub(pattern, repl, value, flags=re.IGNORECASE)

def cleaning_income(value):
    if not isinstance(value, str):
        value = str(value)
    value = value.strip().lower()

    # 1️⃣ Convert words like "thirty thousand"
    try:
        value = w2n.word_to_num(value)
        num_value = float(value)
        if num_value < 0 or num_value > 1000000 or num_value < 1000:
            manual_review.append(num_value)
        return num_value
    except:
        pass

    # 2️⃣ Lakh cleaner
    value = cleaning_inconsistent(value)

    # 3️⃣ Replace K/KK/kk with 000
    value = re.sub(r'(?<=\d)\s*k+', '000', value, flags=re.IGNORECASE)

    # 4️⃣ Remove currency prefixes
    for prefix in currency_prefixes:
        if value.startswith(prefix):
            value = value[len(prefix):].strip()

    # 5️⃣ Remove extra spaces
    value = value.replace(' ', '')

    # 6️⃣ Catch null keywords
    if value in ['', 'nan', 'none', 'null', '--', 'notdisclosed', 'unknown']:
        return np.nan

    # 7️⃣ Convert to float and validate range
    try:
        num_value = float(value)
        if num_value < 0 or num_value > 1000000 or num_value < 1000:
            manual_review.append(num_value)
        return num_value
    except:
        return np.nan

# Apply cleaning
manual_review.clear()
df['income'] = df['income'].apply(cleaning_income)

# Drop invalid rows
df = df.dropna(subset=['income'])

# Show manual review values
print("⚠ Manual Review Required:")
print(manual_review)

# Final cleaned DataFrame
df