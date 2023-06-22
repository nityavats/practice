#lst = [10, 11, 12, 13, 14, 15]
lst=list(input("enter").split(","))
lst.reverse()
print("Using reverse() ", lst)
 
print("Using reversed() ", list(reversed(lst)))