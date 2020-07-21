import subprocess
import time
 

code_dic = { 'A':'.- ', 'B':'-... ','C':'-.-. ','D':'-.. ',
             'E':'. ','F':'..-. ','G':'--. ','H':'.... ',
             'I':'.. ', 'J':'.--- ', 'K':'-.- ','L':'.-.. ',
             'M':'-- ', 'N':'-. ','O':'--- ','P':'.--. ',
             'Q':'--.- ','R':'.-. ','S':'... ', 'T':'- ',
             'U':'..- ', 'V':'...- ','W':'.-- ','X':'-..- ',
             'Y':'-.-- ', 'Z':'--.. ','1':'.---- ', '2':'..--- ',
             '3':'...-- ','4':'....- ', '5':'..... ', '6':'-.... ',
             '7':'--... ', '8':'---.. ', '9':'----. ','0':'----- ',
             ', ':'--..-- ', '.':'.-.-.- ','?':'..--.. ', '/':'-..-. ',
             '-':'-....- ','(':'-.--. ', ')':'-.--.- '}



def txt_morse_code():
    text = input ("enter text to convert to morse code\n")
    code = [code_dic[x.upper()] + ''for x in text if x.upper() in code_dic.keys()]
    morse = "".join(code)
    print(morse)
    
    for s in morse:
        if s=='.':
            subprocess.call(["afplay","bip.mov"])
            
        elif s=='-':
            subprocess.call(["afplay","dash.mov"])
        else:
            time.sleep(1)
            
 
 
def morse_to_txt():
    text = input ("enter morse code to convert to text\n")
    trans = [o for k in text.split() for o,v in code_dic.items() if k==v]
    newtxt = "".join(trans)
    print(newtxt)
    


morse_to_txt()
txt_morse_code()


