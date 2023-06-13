def question_1():
    name = input("Name: ")
    out_file = open("name.txt", 'w')
    print(name, file=out_file)
    out_file.close()

def question_2():
    in_file = open("name.txt", 'r')
    name = in_file.read()
    in_file.close()
    print(name)










# question_1()
question_2()