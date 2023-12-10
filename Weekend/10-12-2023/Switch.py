v1=int(input("Eneter the  value b/t 1-12"))

match v1:
    case 1 : print("January")
    case 2: print("Febuary")
    case _: print("Invalid")

match (v1%2):
    case 0: print("Even")
    case _: print("Odd")
