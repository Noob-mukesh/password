import string,  random

ran1=string.ascii_uppercase
#print(ran1)
ran2=string.ascii_lowercase
ran3=string.punctuation
ran4=string.digits
password=int(input('Enter Password length\n'))
ran=[]
ran.extend(list(ran1))
ran.extend(list(ran2))
ran.extend(list(ran3))
ran.extend(list(ran4))
#print(ran)
print('Your Password is:\n')
random.shuffle(ran)
print("" .join(ran[0:password]))
