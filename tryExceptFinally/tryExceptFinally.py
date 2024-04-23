# This is a method for testing code and preventing crashes
# try -- ecept -- else -- finally

try: # the code in this block is ALWAYS executed.
    myVariable = 1
    print(myVariable)
except NameError: # this code will run IF there is an error (exception) raised.
    print("let there be name error")
except:
    print("i don't know what happened you're on your own")
else:
    print("you gots it good\n")
finally: # always goes
    print("test done")