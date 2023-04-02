# 3.2 CONTADOR DE SILABAS 
# Se tienen tres textos almacenados en tres variables como strings. 
# Para cada texto debes contar cuántas veces se repite la sílaba indicada y qué índice ocupa cada repetición.
# x: “at”
# y: “om”
# z: “in”
# Output:
# x:
# Índices: 13-14, 29-30, 104-105, 112-113
# Repeticiones: 4
# y:
# Índices: 12-13, 19-20, 335-336
# Repeticiones: 3
# z:
# Índices: 6-7, 104-105, 171-172, 203-204, 237-238, 371-372, 414-415
# Repeticiones: 7

# x = "Outside of that, Hu argues that the royalties can be more reliable than the entropy of Wall Street. No matter what happens to the stock market, people are always going to be listening to music."
# y = "CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
# z = "According to a report published by Fast Company, apparel sales have plummeted by 50 percent. It’s a margin that will be difficult to recover from, especially for small businesses that don’t have the backing of major conglomerates. These independent companies rely on seasonal buys from retailers to stay afloat. But with the bevy of store closures and restrictions on online sales, these behemoth retailers are facing hard times of their own."

x = "Outside of that, Hu argues that the royalties can be more reliable than the entropy of Wall Street. No matter what happens to the stock market, people are always going to be listening to music."
y = "CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
z = "According to a report published by Fast Company, apparel sales have plummeted by 50 percent. It’s a margin that will be difficult to recover from, especially for small businesses that don’t have the backing of major conglomerates. These independent companies rely on seasonal buys from retailers to stay afloat. But with the bevy of store closures and restrictions on online sales, these behemoth retailers are facing hard times of their own."

print("x:")
print("\tIndices: ")
for i in range(len(x)):
    if ((x[i]).lower() == "a") and ((x[i+1].lower() == "t")):
        print(f"\t\t* {i}-{i+1}")
print(f"\tRepeticiones: {x.count('at')}")

print("\n")

print("y:")
print("\tIndices:")
for i in range(len(y)):
    if ((y[i]).lower() == "o") and ((y[i+1]).lower() == "m"):
        print(f"\t\t* {i}-{i+1}")
print(f"\tRepeticiones: {y.count('om')}")

print("\n")

print("z:")
print("\tIndices:")
for i in range(len(z)):
    if ((z[i]).lower() == "i") and ((z[i+1]).lower() == "n"):
        print(f"\t\t* {i}-{i+1}")

print(f"\tRepeticiones: {z.count('in')}")