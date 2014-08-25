import random

def decbin(x):
    ans=''
    if x==0:
        ans+='0'
    else:
        while x!=0:
            mod=x%2
            ans+=str(mod)
            x/=2
    return ans[::-1]

def dechex(x):
    ans=''
    if x==0:
        ans+='0'
    else:
        hex='ABCDEF'
        while x !=0:
            mod=x%16
            if mod >=10:
                ans+=str(hex[mod-10])
            else:
                ans+=str(mod)
            x/=16
    return ans[::-1]
def decoct(x):
    ans=''
    if x==0:
        ans+='0'
    else:
        pwr=len(str(x))
        div=x
        while pwr > -1:
            rem=div/8**pwr
            ans+=str(rem)
            div=div-8**pwr * rem
            pwr-=1
    return ans

X=True
bin=0
oct=0
hex=0
while X:
    a=random.randrange(0,100)
    b=random.randrange(0,100)
    x=random.randrange(0,100)
    y=random.randrange(0,100)
    z=random.randrange(0,100)
    op=''
  
    if min(x,y,z)==x:
        num=decbin(min(a,b))
        num2=decbin(min(a,b)+2)
        num3=decbin(min(a,b)+1)
        op='binary'
    elif min(x,y,z)==y:
        num=dechex(min(a,b))
        num2=dechex(min(a,b)+2)
        num3=dechex(min(a,b)+1)
        op='hex'
    elif min(x,y,z)==z:
        num=decoct(min(a,b))
        num2=decoct(min(a,b)+2)
        num3=decoct(min(a,b)+1)
        op='octal'
    
    print(str(min(a,b))+' in '+op+' is?')
    if min(a,b)==a:
        val1=num
        val2=num2
        rig='a'
    elif min(a,b)%2==0:
        val1=num3
        val2=num2
        rig='c'
    else:
        val1=num2
        val2=num
        rig='b'
    print('a)'+str(val1))
    print('b)'+str(val2))
    print('c)None of above')
    inputt=raw_input('Enter your answer [a/b/c] : ')
    if  inputt!=rig:
        X=False
        print('')
        print('oops! that is incorrect..you lose.')
        print('Your score is '+str(bin+oct+hex)+ '[B='+str(bin)+'|O='+str(oct)+'|H='+str(hex)+'].')
    elif inputt!='a' and inputt!='b' and inputt!='c':
        X=False
    if  inputt==rig:
        if op=='binary':
            bin+=1
        elif op=='octal':
            oct+=1
        elif op=='hex':
            hex+=1
