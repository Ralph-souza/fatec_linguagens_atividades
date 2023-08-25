unit_price = float(input("Insira o preco do produto: "))
sales_volume = int(input("Insira a quantidade de vendas: "))
discount_value = float(input("Insira o valor de desconto: "))

sales = unit_price * sales_volume

discount = (sales * discount_value) / 100

result = sales - discount

print(f"O valor de venda é de: {result:.2f}")
