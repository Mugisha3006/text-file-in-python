path_file = "skimming.txt"

#open file in read mode
skimming = open(path_file, "r")

#read file line by line
line1 = skimming.readline()
line2 = skimming.readline()

#print the lines
print(line1)
print(line2) 