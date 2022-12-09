f = open("F:\lingaraj1234.txt","a")

f.write("""
Lorem Ipsum is simply dummy text 
of the printing and typesetting industry. 
Lorem Ipsum has been the industry's 
standard dummy text e
but also the 
""")

if f:
    print("Content added inside the file.")
else:
    print("Content is not written.")

f.close();