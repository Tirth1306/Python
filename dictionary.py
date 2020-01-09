Word={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

num=input("Enter Number : ")

num_list=list(num)

for i in num_list:
    print(f'{Word[i]} ', end='')

