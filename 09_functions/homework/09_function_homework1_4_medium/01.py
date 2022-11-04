

def special_multiplication(string):
    result = ''
    for idx, char in enumerate(string):
        result += char * (idx+1)
    return result


print(special_multiplication('abcxf'))
# abbcccxxxxfffff
