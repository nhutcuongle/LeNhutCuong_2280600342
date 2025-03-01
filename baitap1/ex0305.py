def demsolanxuathien(lst):
    countdict = {}
    for item in lst:
        if item in countdict:
            countdict[item] += 1
        else:
            countdict[item] = 1
    return countdict
inputstring = input("nhap danh sach cac so cach nhau bang dau phay: ")
wordlist = inputstring.split()
solanxuathien = demsolanxuathien(wordlist)
print("so lan xuat hien cua cac phan tu:", solanxuathien)

