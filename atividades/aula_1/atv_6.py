grade_1 = float(input("Insira a primeira nota: "))
grade_2 = float(input("Insira a segunda nota: "))

weight_1 = 4
weight_2 = 6

weighted_average_1 = grade_1 * weight_1
weighted_average_2 = grade_2 * weight_2

average = (weighted_average_1 + weighted_average_2) / (weight_1 + weight_2)

print(f"A média do aluno é de: {average}")
