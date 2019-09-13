for i in range(100):
    if(i%5==0 and i%7==0 and i%13==0):
        print("Multiple of 5 and 7 and 13!")
    elif(i%5==0 and i%7==0):
        print("this is a Multiple of 5 and 7!")
    elif (i % 5 == 0 and i % 13 == 0):
        print("this is a Multiple of 5 and 13!")
    elif (i % 7 == 0 and i % 13 == 0):
        print("this is a Multiple of 7 and 13!")
    elif(i%5==0):
        print("5 is a Multiple of 5!")
    elif (i % 7 == 0):
        print("7 is a Multiple of 7!")
    elif (i % 13 == 0):
        print("13 is a Multiple of 13!")