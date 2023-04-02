with open("test1.txt","a") as file:
    file.write("texto") # ahi puede ir variables 
    file.close()

with open("test1.txt","r") as file:
    x = file.readlines()
    y = []

    for i in x:
        y.append(i.split(","))

    try:
        for i in range(0,len(y[0])):
            print("nombre: " + y[0][i] + " ci:" + y[1][i])
    except:
        pass



# que quiero hacer con el archivo
# r --> read
# a --> append
# w --> write