# Author: Shyama Arunachalam


def singleNumber(nums):
    answer = 0
    for num in nums:
        answer = answer ^ num
    return answer


