a = "Hello World."

print(a)

print(a[6])

print(a[1:5])

# strip() = it removes spaces from beginning and end

x = "  QWERTY KEYPAD  "
print(x)
print(x.strip())

#len() = it return length of given string

print(len(x))

#lower() = it return a string in small letters

x = "Aeroplane"

print(x.lower())

#upper() = it return a string in block letters

print(x.upper())

#replace = it returns replace character or word.

x = "TERM INAL"

print(x.replace('TERM','t'))

#split() = it splits the string into substring if it finds the separator

x = "Term, Inal"

print(x.split(","))

d = input("Enter Your Name: ")

print("Hello" , d," welcome to python class. ")