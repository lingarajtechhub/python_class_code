x = 5
try:
    z = x/0
    print(z)
except:
    print("Divison by zero raise error.")
finally:
    print("Finally always be executed.")
