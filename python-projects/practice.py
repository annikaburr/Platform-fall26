class Practice:

    str = "ihateher"
    if "love" in str:
        print(True)
    else:
        print(False)

    string = "Annika Burr"
    first_name = string[:6]
    print(first_name)

    nums= [1,4,6,9,7,2,8,5]
    i = 0
    total = 0
    while i < len(nums):
        if nums[i] == 6:
            i += 1
            while nums[i] != 8:
                i +=1
            i += 1
        else:
            total += nums[i]
            i += 1
    print(total)

    print (max(nums) - min(nums))
    print(abs(min(nums) - max(nums)))
    print (sum(1 for num in nums if num == 8 or num == 7))

    sentence = "Today is a beautiful day"
    print(sum(1 for char in sentence if char == 'a'))

 
    
                