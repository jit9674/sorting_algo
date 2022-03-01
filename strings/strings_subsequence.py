def subsequence(str1,str2):
    n=len(str1)
    m=len(str2)
    i=0
    j=0
    while (i<n and j<m):
        if (str1[i]==str2[j]):
            j+=1
        i+=1
    return j==m

str1="FINLAND"
str2="NN"

print("Yes" if subsequence(str1,str2) else "No")
