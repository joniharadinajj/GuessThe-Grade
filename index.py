# a = 5
# b = 10
# if (a < b):
#     print("A eshte me e vogel se B")

# x = input("bukurosh/e a mundesh me jep ni numer:")
# if (int(x) > 0):
#     print(f"{x} eshte me i madh se 0")

# x = input("bukurosh/e a mundesh me jep ni numer:")
# if(int(x) > 0):
#     print(f"{x} eshte me i madh se 0")
# elif(int(x) <= 0):
#     print(f"{x} eshte me i vogel se 0")

x = int(input("Shkruaj piket tuaja:"))
if(0 <= (x) <= 29):
    print("Nota 1, pamjaftueshem!")
elif((x>= 30) and (x<= 49)):
    print("Nota 2, mjaftueshem!")
elif((x >= 50) and (x <= 69)):
    print("Nota 3, mire!")
elif((x >= 70) and (x <= 89)):
    print("Nota 4, shume mire!")
elif((x >= 90) and (x <= 100)):
    print("Nota 5, shkelqyeshem!")
