# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

def find_num(list1):
    for i in range(1, len(nums_list)):
        if nums_list[i] - 1 != nums_list[i - 1]:
            return nums_list[i - 1] + 1


with open('G:/Seminars/Python/PythonCourse/Seminar5/numbers.txt', 'r', encoding='utf8') as nums:
    nums_list = list(map(int, nums.read().split()))

print(find_num(nums_list))


                
