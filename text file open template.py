import os as Os
#print(Os.getcwd())
DataFromFile = open("/Users/dan/Desktop/Test121.txt","r")
contents = DataFromFile.read()
print(contents)