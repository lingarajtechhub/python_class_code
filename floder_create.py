import os
#os.rmdir("F:\Lingaraj")
if os.path.exists("F:\lingaraj1234.docx"):
    os.remove("F:\lingaraj1234.docx")
else:
    print("File is not present.")