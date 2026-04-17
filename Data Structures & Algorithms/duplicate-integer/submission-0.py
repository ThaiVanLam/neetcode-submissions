class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #lấy một số bất kỳ
        #kiểm tra số đó có nằm trong các số còn lại hay không
        curr_list = []
        for i in nums:
            if i in curr_list:
                return True
            curr_list.append(i)
        return False

            
        