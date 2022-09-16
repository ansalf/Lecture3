# Lowercases string before comparing

#fungsi .lower() yaitu untuk menjadikan teks menjadi huruf kecil
answer = input("Do you agree? ").strip().lower()
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")
