class mod1:
    """This is Open-Read or Open-Write Class"""
    def __init__(self,path):
        self.path = path
    def Read_Only(self,fname):
        self.fname = self.path+'\\'+fname
        fp = open(self.fname)
        print(fp.read())
        fp.close()
    def Read_Write(self,fname):
        self.fname=self.path+'\\'+fname
        fp = open(self.fname,'r+')
        fp.read()
        fp.write('\n')
        print("Write :wq to stop\n")
        while True:
                data = input()
                if data.lower() == ':wq' :
                    break
                fp.write(data+'\n')
    def __del__(self):
        del self

def main():
    print("\nChoices : \n1.Read only\n2.Read Write\n3.Exit")
    obj1 = mod1(path)
    ch = int(input("Your Choice : "))
    if ch == 1 :
        obj1.Read_Only(fname)
        main()
    elif ch == 2 :
        obj1.Read_Write(fname)
        main()
    elif ch == 3 :
        print("Thanks for using our program")
        exit(0)
    else :
        print("Invalid Choice \nTry Again")
        main()

if __name__ == "__main__" :
   
    print("\nWelcome Sbse Ghatiya Text Editor\n")
    path = input("Enter Path to locate file : ")
    fname = input("Enter File Name to Open that file : ")
    main()
