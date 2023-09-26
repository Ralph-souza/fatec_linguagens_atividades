student = input("Informe o nome do aluno: ")
grade_1 = float(input("Informe a nota da P1: "))
grade_2 = float(input("Informe a nota da P2: "))

average = (grade_1 + grade_2) / 2

if average >= 6:
    print(f"""O aluno {student} possui média de {average} estando assim APROVADO!""")
elif average >= 4 and average >= 5:
    print(f"""O aluno {student} possui média de {average} estando assim de EXAME!""")
else:
    print(f"""O aluno {student} possui média de {average} estando assim REPROVADO!""")
