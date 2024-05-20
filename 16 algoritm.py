def son (nums):
    for i in range(len(nums)-1):
      if  nums[i]==2 and nums[i+1]==2:
         return True
    return False
print(son([1,2,3,4,3]))
