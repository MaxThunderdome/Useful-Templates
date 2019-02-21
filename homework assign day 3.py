location = input("Please Enter a File location")
DataFromFile = open(location,"r")
contents = DataFromFile.read()
print(contents)
#histogram

import matplotlib.pyplot as plt
N_points = 10000
n_bins = 10