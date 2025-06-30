import re
import pandas as pd

# 1. Regex patterns
sample_texts = {
    "email": "test.user123@example.co.in",
    "phone": "+91-9876543210",
    "alphanumeric": "abc123XYZ",
    "zipcode": "400001",
    "url": "https://www.example.com"
}

patterns = {
    "email": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    "phone": r'^(\+91[\-\s]?|0)?[6-9]\d{9}$',
    "alphanumeric": r'^[a-zA-Z0-9]+$',
    "zipcode": r'^\d{6}$',
    "url": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
}

for label, pattern in patterns.items():
    text = sample_texts[label]
    match = re.match(pattern, text)
    print(f"{label.capitalize()} valid: {bool(match)}")

# 2. Pandas datetime functions
data = {
    "order_id": [101, 102, 103, 104],
    "order_date": ["2023-01-15", "2023-02-10", "2023-03-12", "2023-03-18"],
    "delivery_date": ["2023-01-20", "2023-02-15", "2023-03-15", "2023-03-22"]
}
df = pd.DataFrame(data)
df["order_date"] = pd.to_datetime(df["order_date"])
df["delivery_date"] = pd.to_datetime(df["delivery_date"])
df["delivery_time_days"] = (df["delivery_date"] - df["order_date"]).dt.days
df["order_month"] = df["order_date"].dt.month
df["is_weekend_order"] = df["order_date"].dt.dayofweek >= 5
print("\nDatetime-based features:\n", df)

# 3. Data cleaning and analysis on CSV
df_csv = pd.read_csv("data.csv")
print("\nInitial shape:", df_csv.shape)
df_cleaned = df_csv.copy()

null_counts = df_cleaned.isnull().sum()
high_null_cols = null_counts[null_counts > 0.3 * len(df_cleaned)].index.tolist()
df_cleaned.drop(columns=high_null_cols, inplace=True)

df_cleaned.dropna(inplace=True)

for col in df_cleaned.select_dtypes(include="object").columns:
    df_cleaned[col] = df_cleaned[col].str.strip()

df_cleaned.columns = [col.lower().replace(" ", "_") for col in df_cleaned.columns]

print("\nCleaned shape:", df_cleaned.shape)

summary = {
    "total_rows": len(df_cleaned),
    "total_columns": df_cleaned.shape[1],
    "numeric_summary": df_cleaned.describe().to_dict(),
    "categorical_counts": {
        col: df_cleaned[col].value_counts().to_dict()
        for col in df_cleaned.select_dtypes(include="object").columns
    }
}

print("\nData Summary:")
print(summary)

if 'date' in df_cleaned.columns:
    df_cleaned['date'] = pd.to_datetime(df_cleaned['date'], errors='coerce')
    df_cleaned['year'] = df_cleaned['date'].dt.year
    df_cleaned['month'] = df_cleaned['date'].dt.month
    df_cleaned['day_name'] = df_cleaned['date'].dt.day_name()

    print("\nTime-based breakdown:")
    print(df_cleaned.groupby('month').size())

if 'amount' in df_cleaned.columns:
    print("\nTop 5 highest amounts:")
    print(df_cleaned.sort_values(by='amount', ascending=False).head())

print("\nData analysis complete.")