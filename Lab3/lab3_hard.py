def my_hash(obj, p=9 ** 17):
    rezult = 0
    for i in range(len(obj)):
        rezult += ord(obj[i]) * (p ** i)
    rezult %= (2 ** 127)
    return str(hex(abs(2 ** 128 - rezult)))[2:]


print(my_hash(list('helloworld')))
