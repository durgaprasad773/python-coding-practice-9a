m=int(input())
n=int(input())
sum_of= 0
for i in range(m,n+1):
    if i % 2 != 0:
        sum_of= sum_of + i
print(sum_of)