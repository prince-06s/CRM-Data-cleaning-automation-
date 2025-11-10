import re
import numpy as np

suspicious_id = []

def clean_id_column(df):
    def cleaning_id(value):
        if not isinstance(value, str):
            value = str(value)

        value = value.strip()
        value = value.replace('o', '0').replace('O', '0')  # typo fix first
        value = value.upper()
        value = re.sub(r'[^0-9A-Z]', '', value)
        value = re.sub(r'([A-Z]+)(\d+)', r'\1  \2', value)
        return value

    # Step 1: Apply cleaning
    df['id'] = df['id'].apply(cleaning_id)

    # Step 2: Normalize NaNs
    df['id'] = df['id'].replace(r'(?i)^nan$', np.nan, regex=True)

    # Step 3: Validation logic
    for value in df['id']:
        if not isinstance(value, str):
            value = str(value)

        value = value.strip().upper()

        is_only_digit = value.isdigit()
        is_toolong = len(value) > 15
        no_alpha = not any(char.isalpha() for char in value)

        if is_only_digit or is_toolong or no_alpha:
            suspicious_id.append(value)

    print("SUSPICIOUS ID:")
    print(suspicious_id)

    # Step 4: Drop duplicates and NaNs
    df = df.drop_duplicates(subset=['id'])
    df = df.dropna(subset=['id'])

    return df