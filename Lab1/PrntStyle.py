#WAP to enter name and age.

userName = str(input('Enter your name: '))
userAge  = float(input('Enter your age: '))
print('Hello my name is ' +userName+ ' and i am '+str(userAge)+' years old')
print('Hello my name is', userName ,'and i am', userAge , 'years old')
print('Hello my name is %s and i am %d years old' % (userName, userAge ))
print('Hello my name is {} and i am {} years old' .format(userName, userAge))

