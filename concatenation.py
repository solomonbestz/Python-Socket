first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
age = int(input("Enter Age: "))
current_year = int(input("Enter Current Year: "))
earthly_appearance = current_year - age

print(first_name + " " + last_name + ", You are "+ str(age) + " years old and you came to Earth In the year "+ str(earthly_appearance))
