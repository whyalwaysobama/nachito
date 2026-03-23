frutas = ["banana", "manzana", "pera"]
fruta1 = input("ingrese su fruta favorita: ")
if fruta1 in frutas:
    print("esa fruta es de mis favorita tambien")
else:
    fruta2 = input("ingrese su fruta favorita: ")
    if fruta2 in frutas:
        print("esa fruta es de mis favorita tambien")
    else:
        fruta3 = input("ingrese su fruta favorita: ")
        if fruta3 in frutas:
            print("esa fruta es de mis favorita tambien")
        else:
            print("ninguna de mis frutas favoritas es tu favorita")