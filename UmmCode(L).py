speech = input()
#speech = "umm ummm Friends uum umm um ummmm u?"
s = speech.split()

#print(s)

temp = ""
msg = ""

for i in range(len(s)):
    temp = ""
    for j in range(len(s[i])):
        #print(s[i][j])
        if (s[i][j] == 'u' or s[i][j] == 'm'):
            temp = temp + s[i][j]
            #print("At s[" + str(i) + "][" + str(j) + "]: temp = " + temp)
        elif (not(s[i][j].isalpha() or s[i][j].isdigit())):
            #print("Punctuation: " + s[i][j])
            continue
        else:
            break
    msg = msg + temp

#print(msg)

bin_msg = ""
num_times = len(msg) / 7
bin_sum = 0
power = 6

for k in range(int(num_times)):
    bin_sum = 0
    power = 6
    for l in range(7):
        if (msg[l + 7 * k] == 'u'):
            bin_sum = bin_sum + 2**power
        power = power - 1
    #print("bin_sum = " + str(bin_sum))
    bin_msg = bin_msg + chr(bin_sum)

print(bin_msg)

