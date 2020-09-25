from googletrans import Translator
q='y'
while(q=='y'):
    t=Translator()
    a=input("enter source language code: ")
    b=input("enter destination language code: ")
    s=input("enter the sentence in source lanuage form: ")
    ts=t.translate(s,src=a,dest=b)
    print(ts.text)
    q=input("do you want to repeat y/n ")
    
