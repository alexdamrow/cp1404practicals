# Question 1

name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Question 2

in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# Question 3

in_file = open("numbers.txt", 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)

# Question 4

in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)









