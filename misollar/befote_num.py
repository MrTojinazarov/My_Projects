nums = str(input("nums = "))

for i in range(len(nums)):
    if nums[i] == " ":
        continue
    else:
        if nums[i] in nums[:i]:
            print("yes")
        else:
            print("no")
    