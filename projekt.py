import pandas as pd

# Załadowanie danych
df = pd.read_csv('winequality-red.csv')

# Sprawdzanie, czy są duplikaty
duplikaty = df.duplicated()

# Wyświetlenie wierszy, które są duplikatami
print(df[duplikaty])
