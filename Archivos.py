x0 = float(input("ingrese coord X0: "))
y0 = float(input("ingrese coord y0: "))
w = float(input("ancho(W): "))
h = float(input("alto(H): "))

salida = open("salida.txt", "w")
salida.write("(" + str(x0) + ", " + str(y0)+ ")" + " w: " + str(w) + "h: " + str(h))

n = 3

while 0 < n:
    punto= input("inresar un punto (x,y): ")
    punto = punto[1:-1].split(",")
    punto[0] = float(punto[0])
    punto[1] = float(punto[1])
    if x0 <= punto[0] and x0 <= punto[0] + w and y0 <= punto[1] and punto[1] <= y0 - h:
        n += 2
        salida.write("()" + str(punto[0]) + ", " + str(punto[1]))
    else:
        print("no cae en el rectangulo")

salida.close()
input()
