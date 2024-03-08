compras=[]
item="tomate, cebolla, queso, aceite, coca cola, agua, melon, sandia, coco, vino"
while True:
    item=input("ingrese un producto de su lista: ")
    if item == "fin":
        break
    else:
        compras.append(item)


print(compras)

while True:
    elim=input("quiere eliminar algo de la lista?: ")
    if elim == "no":
        break
    elif elim == "si":
        item_elim = input("que desea eliminar?: ")
        if item_elim == "fin":
            break
    else:
        print(compras)
        break