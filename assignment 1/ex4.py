a = float(input("Edge length: "))
print("Surface: " + str(round((a ** 2 * 3**(1/2)), 4)))
print("Volume: " + str(round(a**3/12*2**(1/2), 4)))
print("Height: " + str(round(a/3*6**(1/2), 4)))