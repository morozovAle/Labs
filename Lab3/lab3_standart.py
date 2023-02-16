def hash(text):
    hash_value = 99999
    result = 0

    for char in text:
        result = (result * 37 + ord(char)) % hash_value
    return result


print(hash(list('helloworld')))