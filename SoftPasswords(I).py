s = input()
p = input()

#print(s)
#print(p)

last = len(s) - 1

if (s == p):
    print("Yes")
elif (len(s) == len(p) + 1):
    if (s[0:last] == p and s[last].isdigit()): # Appended digit
        print("Yes")
    elif (s[1:len(s)] == p and s[0].isdigit()): # Prepended digit
        print("Yes")
    else:
        print("No")
elif (s == p.swapcase()):
    print("Yes")
else:
    print("No")
