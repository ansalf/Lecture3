# Strips string before comparing

#fungsi .strip() yaitu menghilangkan spasi yang tidak perlu
answer = input("Do you agree? ").strip()
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")
