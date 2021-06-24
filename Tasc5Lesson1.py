# Task5Lesson1
# финансовым результатом.

venit = int(input("Introduceti vanzarile: "))
cheltuili = int(input("Introduceti cheltuielile: "))
profit =venit-cheltuili;
if profit<0:
    print(f"compania activeaza cu pirderi {profit}");
else:
    print(f"compania activeaza cu pazitiv {profit}");
    rentab = profit/venit*100//1; print(f"Rentabilitatea activitatii constituie {rentab} %")
    nr_angajati = int(input("Introduceti numarul salariatilor: "))
    profit_angajat = profit/nr_angajati//1; print(f"profitul la un angajat constituie {profit_angajat} mdl")
