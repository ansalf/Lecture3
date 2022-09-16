# Compares multiple strings

answer = input("Do you agree? ").strip().lower()
#kita perlu memeriksa karakter awal pada sebuah string apakah sesuai keinginan kita atau tidak
if answer.startswith("y"):
    print("Agreed")
else:
    print("Not agreed")
