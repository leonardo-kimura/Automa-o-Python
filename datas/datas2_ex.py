from datetime import datetime

agora = datetime.now()
data = datetime(2025, 12, 31)
dias_restantes = data - agora
print(f"Faltam {dias_restantes.days} dias para {data.day}/{data.month}/{data.year}")
