


from ast import Return


def hello():
    print("Hello,World!")

    def pack (a,b,c):
    return  [a,b,c]

    def eat_lunch(my_1st):
        if len(my_1st) == 0:
            print("My lunchbox is empty!")
            else: 
                for i in range(len(my_1st)):
                    if i ==0: 
                        print(f"First I eat {my_1st[0]}")
                        else:
                            print(f"Next I eat{my_1st[i]")