n = int(input("Enter the amount of items in the list: "))
k = int(input("Enter k: "))
nums = []
x = 1
while x <= n:
    nums.append(int(input("Enter element: ")))
    x += 1



for i in range(len(nums) - 1):
    behind = i - 2
    ahead = i + 2
    if behind >= 0 and nums[behind] > nums[i]:
        nums[i], nums[behind] = nums[behind], nums[i]
    if ahead <= len(nums) - 1 and nums[ahead] < nums[i]:
        nums[i], nums[ahead] = nums[ahead], nums[i]
    
print(nums)