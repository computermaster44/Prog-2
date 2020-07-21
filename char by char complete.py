import re
a = input('Enter First Name: ')
b = input('Enter Last Name: ')
c = input('Enter Age: ' )
d = input('Enter Balance: ')
age = int(re.sub('[^0-9]', '', c ))


def data():
    global dato 
    global ad 
    global i 
    global j
    global g
    global mi
    ad = ('Adult')
    mi = ad.replace('Adult','Minor')
    dato = 0
    
    g = input('Enter Gender : M = Male / F = Female :\n')
    if g == 'f':
        dato+= 1
    
    if age > 17:
        dato+= 2 
    
    
    i = input('Enter if you have a Drivers License : y = yes / n = no\n')
    if i == 'y':
        
        dato+= 4
    
    j = input('Enter if you have a Vehicule : y = yes / n = no\n')
    
    if j == 'y':
        dato+= 8
        

    
    


data()
e = input('Enter password: ')
f = input('Re-enter password: ')
balance = re.sub('[^0.0-9.9]', '', d )



def correct():   
    
    print('\nWELCOME :'+ a,b)
    
    print("\nFirst Name: " + a, '\nLast Name: ' + b,'\nAge: ' + str(age),
          '\nGender: ' + g,'\n')
    
    if age > 17:
        print(ad)
    else:
        print(mi)
    
    #Mm()
    
    print('\nBalance:' + balance, '\n Drivers License: ' + i,
          '\nVehicule: ' + j, '\nPassword:' + e, '\n' + str(dato))



q = 5
for x in range(q):

    while(f!= e):
        
        x = x+1
        print('\nWRONG PASSWORD')
        print (q - x, 'attempts left')
    
        f = input('Re-enter password:')

        break
    
    else:
        correct()
        
        break








