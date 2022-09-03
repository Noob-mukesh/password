# Dear Piro Plz Dont remove this line 
# By @itz_mst_boi
# source:-  https://github.com/Noob-mukesh/password
import string,  random
ran1=string.ascii_uppercase
#print(ran1)
ran2=string.ascii_lowercase
ran3=string.punctuation
ran4=string.digits
print("Tools to generate Random Password using Termux")
print(" Hint ? Password Strength \n [1-test , 2-lowest , 3-lower ]\n[ 4- low 5-Normal , 6-Strong] \n[ 7- strongest, 8-very-Strong]\n")
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
print(" Join @Mukeshbotzone for More  By @itz_mst_boi")
