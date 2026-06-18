nested_list= [ [1,2,3],[4,5,6],[7,8,9]]
res = [val for sublist in nested_list for val in sublist]
print(res)
