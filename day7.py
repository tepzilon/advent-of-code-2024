import sys


def find_solution(nums, target, result):
    if len(nums) == 0:
        return result == target
    found_if_plus = find_solution(nums[1:], target, result + nums[0])
    found_if_multiply = find_solution(nums[1:], target, result * nums[0])
    return found_if_plus or found_if_multiply


sum = 0
for line in sys.stdin:
    (target, nums) = (part.strip() for part in line.split(":"))
    target = int(target)
    nums = [int(n.strip()) for n in nums.split(" ")]
    if find_solution(nums, target, 0):
        sum += target
print(sum)
