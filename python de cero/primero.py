def main():
    nombrebien = pri()
    seg(nombrebien)


def pri():
    nombre = input("como te llamas: ")
    nombrebien = nombre.capitalize()
    if nombre.isalnum():
        return nombrebien    
    else:
        exit(0)

def seg(nombrebien):
    print(f"tu nombre es {nombrebien}")

main()