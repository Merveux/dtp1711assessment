nums = 
for i in range(1, 21):
    nums.append(i)
nums = [n for n in nums if n % 2 == 0]
nums.sort(reverse=True)
top_three = nums[:3]
print("Top 3 numbers:", top_three)
