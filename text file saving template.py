import os as Os
print(Os.getcwd())
outFile = open("Test121.txt","w")
outFile.write("There is some text")
outFile.close()