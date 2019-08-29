string=input("Enter String:")

if __name__=="__main__":
    def palindrom(string):
        left,right=0,len(string)-1
        while right>=left:
            if not string[left]==string[right]:
                return False
            left+=1;right-=1
        return True
print(palindrom(string))



