def subsequence(str1,str2,n,m):
    if m==0:
        return True
    if n==0:
        return False

    if (str1[n-1]==str2[m-1]):
        return (subsequence(str1,str2,n-1,m-1))
    return (subsequence(str1,str2,n-1,m))

str1="ICELAND"
str2="LAN"
n=len(str1)
m=len(str2)
print("Yes" if subsequence(str1,str2,n,m) else "No")