# coding=utf-8

def print_everything(*arg):
    for count,thing in enumerate(arg):
        print ('{0}.{1}'.format(count,thing))

def print_kwargs(**kwargs):
    for key in kwargs:
        print ('{0}={1}'.format(key,kwargs[key]))

def print_kw(name="jks",age=23):
    print ('{0}={1}'.format(name,age))
        
if __name__=="__main__":
    kes=(["jang","kdng",20],"nag"),"nd"
    print_everything(kes)
    print_kwargs(name="kg",age=20)
    jks={"age":18}
    print_kw(**jks)
    import os
    print (os.getcwd())
    #os.mkdir("cs")
    #os.makedirs("css//cs//jks//jks")
    print os.path.dirname(os.path.abspath('__file__'))
    print os.listdir("os.path.dirname(os.path.abspath('__file__'))")

    
    
    
