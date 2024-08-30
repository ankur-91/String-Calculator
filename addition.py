import re


class NegativeNumberError(Exception):
    def __init__(self, n):
        super().__init__(f"Negative numbers not allowed: {n}")

def add(li):
    res = 0
    negative_numbers = []

    try:
        for n in li:
            n = int(n)
            if n < 0:
                negative_numbers.append(n)
                raise NegativeNumberError(n)
            res += int(n)
        return res
    except NegativeNumberError as e:

        print(e)


def addition(st):

    if st.startswith('\\'):
        cleaned_st = re.sub(r"^[^\d]*\n", "", st)
        cleaned_st = re.sub(r"^[^\d]*", "", cleaned_st)


    second_split = re.split('\n|,', cleaned_st)
    print(second_split)
    result = add(second_split)
    return result

s = '\\;n*1,2,3'
print(addition(s))