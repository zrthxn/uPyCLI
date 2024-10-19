from upycli import command

@command
def func(arg1: list, arg2: list = ["Bye"]):
    print(arg1)
    ...