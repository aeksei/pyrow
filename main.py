from pyrow import pyrow


if __name__ == '__main__':
    #Connecting to erg

    ergs = list(pyrow.find())
    if len(ergs) == 0:
        exit("No ergs found.")
    erg = pyrow.PyErg(ergs[0])
    print("Connected to erg.")

    erg.set_workout(distance=2000, split=100, pace=120)

