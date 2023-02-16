import string

alf1 = "abcdefghijklmnopqrstuvwxyz"
alf2 = "qwertyuiopasdfghjklzxcvbnm"


def crypt(text, alf1, alf2):
    result = ""

    for i in text:
        if i != " ":
            j = alf1.find(i)
            result = result + alf2[j]
        else:
            result = result + " "
    return result


in_string = "hello world"
out_string = crypt(in_string, alf1, alf2)
dec_string = crypt(out_string, alf2, alf1)

print(in_string)
print(out_string)
print(dec_string)