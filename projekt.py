import pandas as pd

# Załadowanie danych
df = pd.read_csv('cleaned_data.csv')

# Wybór tylko kolumn liczbowych
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Normalizacja Min-Max za pomocą Pandas
df[numeric_columns] = df[numeric_columns].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

# Sprawdzenie wyników
print(df.describe())

# Zapisanie znormalizowanych danych do nowego pliku CSV
df.to_csv('normalized_cleaned_data.csv', index=False)
