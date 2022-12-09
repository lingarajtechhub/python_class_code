"""import os
os.mkdir("D:\Abhijeet")
"""
"""
f = open("D:\Abhijeet\Abhijeet.txt", "xt")
f.write("This is a file content.")
f.close()
"""
"""
f = open("D:\Abhijeet\c1.txt", "x")
f = open("D:\Abhijeet\c1.txt", "w")
f.write("This is a c1 file.")
f.close()"""

"""
f = open("D:\Abhijeet\c1.txt", "r")
print(f.read())
f.close()"""

"""
f = open("D:\Abhijeet\c1.txt", "a")
f.write("This is a append content.")
f.close()"""
"""
f = open("D:\Abhijeet\c1.txt", "r")
print(f.read())
f.close()"""
"""
#File content erase.
f = open('D:\Abhijeet\c1.txt', 'r+')
f.truncate(0)
f.close()
"""
import os
#os.remove("D:\Abhijeet\Abhijeet.txt")

os.rmdir("D:\Abhijeet")