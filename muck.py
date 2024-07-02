from datetime import datetime

print("Example 1, getting the lot")
birthday = "21/06/1974"
my_bith = datetime.strptime(birthday, "%d/%m/%Y")
print(my_bith)

print("Example 2, just getting a date")
birthday = "21/06/1974"
my_bith = datetime.strptime(birthday, "%d/%m/%Y").date()
print(my_bith)

print("Example 3 getting year")
birthday = "21/06/1974"
my_bith = datetime.strptime(birthday, "%d/%m/%Y").year
print(my_bith)

print("Example 4, getting month")
birthday = "21/06/1974"
my_bith = datetime.strptime(birthday, "%d/%m/%Y").month
print(my_bith)

print("Example 5, getting day")
birthday = "21/06/1974"
my_bith = datetime.strptime(birthday, "%d/%m/%Y").day
print(my_bith)
