string=list(input("Enter String :"))
temp = ""
for i in range(1,len(string)):
    if(string[i-1]==string[i]) or string[i]==temp:
        string[i] = '*'
    else:
        temp = string[i]

for i in string:
    print(i, end="")


# print (string)

