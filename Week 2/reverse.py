def reverse(s):
    result = " "
    for c in s:
        result = result + c

    return result

t = raw_input("Please enter a string ")
print("The reverse of", t, "is", reverse(t))
