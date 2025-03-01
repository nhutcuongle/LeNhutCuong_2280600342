def xoaphantu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keytodelete = 'b'
result = xoaphantu(mydict, keytodelete)

if result:
    print("phan tu dã được xoá Dictionary:", mydict)
else:
    print("khong tìm thấy ptu xoá trong Dictionary.")