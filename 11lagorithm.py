def count_evens(nums):
    son_sanagich=0
    for i in  nums:
       if i %2==0:
           son_sanagich+=1
    return son_sanagich
nums=[1,2,3,4,5,6,7,8,9]
print(count_evens(nums))      