def reverse_v2(s):
    result=''
    
    for c in s:
        result=c+result

    return result

def reverseprint(mystring):
    '''reverse s and then print each character of the reversed string\n 
on a new line'''

    #which version of the reverse function should we use?
    
    reverse_string = reverse_v2(mystring)
    for letter in reverse_string:
        print letter
       
    return None

    #used reverse_v2 because it returns the modified result
    #reverse_v1 only prints it and returns None

mystring = raw_input('enter str: ')
execute = reverseprint(mystring)
    #had to define mystring outside of function in order \
    #to properly execute function
    #added a variable to call function automatically
