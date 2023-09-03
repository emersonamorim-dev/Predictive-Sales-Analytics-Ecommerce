import pandas as pd
import random
from datetime import datetime, timedelta

# Dados fictícios de produtos
products = {
    "smartphone": [100, 150, 500],
    "laptop": [30, 50, 1000],
    "headphone": [150, 250, 50]
}

# Data inicial
start_date = datetime(2023, 1, 1)
end_date = start_date + timedelta(days=365)

data = []

# Gere dados fictícios para cada dia e produto
current_date = start_date
while current_date <= end_date:
    for product, details in products.items():
        units = random.randint(details[0], details[1])
        total_sales = units * details[2]
        data.append([current_date, product, units, details[2], total_sales])
    current_date += timedelta(days=1)

# Crie um DataFrame pandas a partir dos dados gerados
df = pd.DataFrame(data, columns=["date", "product", "units_sold", "price_per_unit", "total_sales"])

# Salve o DataFrame como um arquivo .parquet
df.to_parquet("sales_data.parquet", index=False)

print("Arquivo 'sales_data.parquet' salvo com sucesso!")
