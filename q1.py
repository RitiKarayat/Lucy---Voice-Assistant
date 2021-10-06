from itertools import combinations 
n = int(input())
l = list(map(int,input().split()))



max_len = len(bin(max(l)))-2
answer = 0


for i in range(n):
    subsets = list(combinations(l,i+1))

    for k in range(len(subsets)):
        num = ''
        b = list(map(bin,subsets[k]))
        final_list = []
        for j in range(len(b)):
            
            digit_len = 0
            digit_len = max_len - len(b[j].replace('0b',''))
            
            final_list.append(b[j].replace('0b',digit_len*'0'))
        num = ''.join(final_list)
        if num.count('0')==num.count('1'):
            answer+=1
result = bin(answer)
ans_len = max_len - len(result.replace('0b',''))
result = result.replace('0b',ans_len*'0')
print(result)

    


  


    


