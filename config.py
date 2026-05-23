

def opens(files):
    f1=open(files,"r")
    f=f1.read()
    f1.close()
    ff=f.split("\n")
    return ff


def lists(s:str):
    ss=s.strip()
    if len(ss)>0:
        if ss[0]=="[":
            sss=ss.replace("[","")
            sss=sss.replace("]","")
            sss=sss.strip()
            print(20*"-")
            print(sss)
            print(20*"-")
        else:
            print (8*" "+ss)
list1=opens("my.txt")
for a in list1:
    lists(a)