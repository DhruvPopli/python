def prime(n,i):
    
    if i==1:
        return True
    else:
        if n%i!=0:
            return prime(n,i-1)
        else:
            return False

n = 6
i = n-1
print(prime(n,i))
        
        
