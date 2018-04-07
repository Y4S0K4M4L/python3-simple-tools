# This simple tool is to delete all the extra files produced by vim when editing

import os

def main():
    dirtw = str(input("Enter the absolute path to work on: "))
    listos = os.listdir(dirtw)
    list2 = []
    for item in listos:
        if dirtw[-1] == "/" or dirtw[-1] == "\\":
            itet = dirtw+item
        else:
            itet = dirtw+"/"+item
        list2.append(itet)


    for item in list2:
        if item[-1] == "~":
            os.remove(item)
        else:
            pass

main()
