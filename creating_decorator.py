def my_first_function(func):
    def my_second_function():
        print("Beginning to execute the function!")
        func()
        print("The function has finished executing!")
    return my_second_function

def greeter():
    print("Hello my name is Dillan, very nice to meet you!")

greeter()

my_first_function(greeter)

greeter = my_first_function(greeter)

greeter()

def dog_talker():
    print("Who is a good boy?")

dog_talker = my_first_function(dog_talker)

dog_talker()