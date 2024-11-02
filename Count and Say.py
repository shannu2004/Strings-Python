def Count(n):
    j=1
    s="1"
    while (j<n):
        count=1
        string=s
        s=""
        for i in range(1,len(string)):
            if string[i]==string[i-1]:
                count+=1
            else:
                s+=str(count)+string[i-1]
                count=1
        s+=str(count)+string[-1]
        j+=1
    return s
n=4
print(Count(n))


#TC: O(2^n)
#SC: O(2^n)
