filenames = ["1.idegas.txt", "2.neidegas.txt", "3.malkoidegas.txt"]

for filename in filenames:
    filename = filename.replace('.','-', 1)
    #file.rename(filename)    // renames on the hard disk
    print(filename)