#Keyword Arguments
def msg(id,name,age):
    print(id," ",name," ",age)

msg(id=324,name="QWERTY",age=43)

def msg(id,name,age=35):
    print(id," ",name," ",age)

msg(id=324,name="QWERTY")