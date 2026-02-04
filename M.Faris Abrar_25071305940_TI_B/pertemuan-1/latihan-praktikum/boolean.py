#
are_student = True
input = input("apakah anda student : ")
if input == "y":
    are_student = True

else:
    are_student = False

if are_student : 
    print("you are a student")

else:
    print("you are not a student")

print(f"you are student: {are_student}")

