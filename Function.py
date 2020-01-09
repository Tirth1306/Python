# def function(greeting,name='tirth'):

#     return '{},{}'.format(greeting,name)


# print(function(4))



# def another(*args,**kwargs):
#     print(args)
#     print(kwargs)

# another('tirth','shrey',7,age='19')


# month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

# def is_leap(year):
    
#     return year%4==0 and (year%100 !=0 or year%400==0)

# def days_in_month(year,month):

#     if 0>month>12 :
#         return print('Enter Valid Month')
    
#     if(month==2 and is_leap(year)):

#         return 29

#     else:
#         return month_days[month]

# print(days_in_month(2019,2))

import os

print(os.getcwd())

os.walk()
