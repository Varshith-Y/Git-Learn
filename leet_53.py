nums = [1,2,2,3,3,3]
counter = 0
count_dict = {}
result=[]
for element in nums:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element]=1
print(count_dict)
reversed_dict= dict(reversed(list(count_dict.items())))
print(reversed_dict)
for num in reversed_dict.keys():
    counter = counter+1
    if counter != 2+1:
        result.append(num)
    else:
        break
print("Crazy Colours")
return(sorted(result))
