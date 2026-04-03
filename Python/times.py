if __name__=="__main__":
    from math import e

    for i in range(1, 21):
        factor = 60/e
        print(i / 20, int(e**(i / 20) * factor))