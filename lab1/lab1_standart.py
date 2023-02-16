import string

alf = 'abcdefghijklmnopqrstuvwxyz'
shift = 15


def crypt(text):
    rez = ""
    for l in text:
        if l != " ":
            i = alf.find(l)
            i = (i + shift + len(alf)) % len(alf)
            rez = rez + alf[i]
        else:
            rez = rez + " "
    return rez


def decrypt(text):
    rez = ""
    for l in text:
        if l != " ":
            i = alf.find(l)
            i = (i - shift + len(alf)) % len(alf)
            rez = rez + alf[i]
        else:
            rez = rez + " "
    return rez

in_string = "hello world"
out_string = crypt(in_string)
dec_string = decrypt(out_string)

print(in_string)
print(out_string)
print(dec_string)