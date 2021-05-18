from os import read


def swapFileData():
    file_Name1 = input("Enter the name of the first file: ")
    file_Name2 = input("Enter the name of the second file: ")
    
    with open(file_Name1,'r') as a:
        data_1 = a.read()
    with open(file_Name2,'r') as b:
        data_2 = b.read()

    with open(file_Name1,'w+') as a:
        a.write(data_2)

    with open(file_Name2,'w+') as b:
        b.write(data_1)
    
swapFileData()