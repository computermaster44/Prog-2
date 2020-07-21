import csv
import re

fn='csvdt.txt'

#separators for each data set
bldate1='0b'
bldate2='0b'
bldate3='0b'
bldate4='0b'
bldate5='0b'

bltemp1='0b'
bltemp2='0b'
bltemp3='0b'
bltemp4='0b'
bltemp5='0b'


with open(fn, 'r') as file:
    reader = csv.reader(file)
    c=0
    r=0
    for row in reader:
        for a in row:
            num=re.split('[-T:.]', a)
            
            for i in num:
                i=int(i)
                #reading column by column Date
            if r in (0,4,8,12,16):
                for n in num:
                    n=int(n)
                    n=bin(n)
                    n=re.sub('0b','',n)
                    c+=1
                    if c<9:
                        bldate1+=n
                    if c>=9 and c<18:
                        bldate2+=n
                    if c>=18 and c<27:
                        bldate3+=n
                    if c>=27 and c<36:
                        bldate4+=n
                    if c>=36:
                        bldate5+=n
                r+=1
                #reading column by column Weather
            else:
                for n in num:
                    n=int(n)
                    n=bin(n)
                    n=re.sub('0b','',n)
                    if r>0 and r<4:
                        bltemp1+=n
                        r+=1
                    if r>4 and r<8:
                        bltemp2+=n
                        r+=1
                    if r>8 and r<12:
                        bltemp3+=n
                        r+=1
                    if r>12 and r<16:
                        bltemp4+=n
                        r+=1
                    if r>16:
                        bltemp5+=n
                        r+=1
                        
                        
bld1=(int(bldate1,2))
bld2=(int(bldate2,2))
bld3=(int(bldate3,2))
bld4=(int(bldate4,2))
bld5=(int(bldate5,2))

blt1=(int(bltemp1,2))
blt2=(int(bltemp2,2))
blt3=(int(bltemp3,2))
blt4=(int(bltemp4,2))
blt5=(int(bltemp5,2))
                
                        
with open('result.csv', 'a', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['Date and Time','Temp',])
    writer.writerow([ bld1,blt1])
    writer.writerow([ bld2,blt2])
    writer.writerow([ bld3,blt3])
    writer.writerow([ bld4,blt4])
    writer.writerow([ bld5,blt5])
    
 
     
#  word = '11111100100111110110011111101100110000011011001100110001011110'
# 
# x = ([word[i:i+7] for i in range(0, len(word), 7)])
# 
# year = x[0]
# month = x[1]
# day = x[2]
# hour = x[3]
# minute = x[4]
# second = x[5]
# milisecond = x[6]
# DayTime1 = x[7]
# DayTime2 = x[8]
# y = (year, month, day, hour, minute, second, milisecond, DayTime1,DayTime2)
# 
# 
# b = [year]
# print(b)           
            
                
           
                
                
            
            
        
