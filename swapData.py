def swapFileData():
    f1=input("enter first file's name: ")
    f2=input("enter second file's name: ")

    f1Data=open(f1).read()
    f2Data=open(f2).read()
    
    print("Before Swapping: ")
    print(f1+" data: "+f1Data)
    print(f2+" data: "+f2Data)

    open(f1,"w").write(f2Data)
    open(f2,"w").write(f1Data)

    print("After Swapping: ")
    print(f1+" data: "+open(f1).read())
    print(f2+" data: "+open(f2).read())

swapFileData()