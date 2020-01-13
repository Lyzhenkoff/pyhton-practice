nums = [1,3,5,1];
for elem in nums:
            if (elem > elem-1) and (elem > 1):
                nums = elem - 2
print(nums)