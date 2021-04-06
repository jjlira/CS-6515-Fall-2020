import findX


for s in range(500):
    try:
        findX.findXinA(s)
    except:
        print("Error on seed {}".format(s))
        break