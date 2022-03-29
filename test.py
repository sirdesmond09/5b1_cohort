def most_frequent(arr, k):
    
    if k > len(arr):
        print("Out of range")
        return
    
    if k <= 0:
        print([])
        return
    
    my_dict = {}
    
    for ele in arr:
        my_dict[ele] = my_dict.get(ele, 0) + 1
    
    sorted_values = sorted(my_dict.items
    (), key = lambda x:x[1], reverse=True)[:k]
    
    print(sorted_values)
    
    
    
    
arr = [10, 11, 11, 13, 12, 140, 15, 12, 13, 13, 15, 15, 15, 15, 140, 140, 140, 140]

most_frequent(arr, 0)
