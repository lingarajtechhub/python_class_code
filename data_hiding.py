class __JustCounter:#PRIVATE CLASS
    __secretCount=0#PRIVATE

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)
    
J = __JustCounter()
print(J)
J.count()
J.count()
J.count()
#print(J.__secretCount)
print(J._JustCounter__secretCount)