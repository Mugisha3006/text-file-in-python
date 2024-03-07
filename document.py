f_p = "document.txt"

#open file in append mode
f = open(f_p, "a")

#add text to the file using the .write() method
addition = f.write("A common way to classify communication is by whether information is exchanged between humans, members of other species, or non-living entities such as computers.")

#close file 
f.close()

#print file
print(addition)

