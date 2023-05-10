class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        try:
            if not target >= -1*10**9:
                return

            if not target < 1*10**9:
                return

            if not len(nums) >= 2:
                return

            if not len(nums) <= 1*10**4:
                return

            if not max(nums) < 1*10**9:
                return

            if not min(nums) > -1*10**9:
                return

            found = False
            a = len(nums) - 1
            while found == False:
                for ind, val in enumerate(nums):

                    if ind == a:
                        a -= 1
                    else:
                        summation = val + nums[a]
                        if summation == target:
                            # print(f'{val=} {nums[a]=}')
                            # print(f'{summation=} = {target=}')
                            found = True
                            return [ind, a]
                        else:
                            # print(f'{ind}, {a}')
                            # print(f'{val=} + {nums[a]=}  = {summation}')
                            pass
            if target == 0:
                # print('found 0')
                index = nums.index(0)
                index2 = nums.index(0, index + 1)
                return [index, index2]

        except ValueError:
            return None

test = Solution()


print(test.twoSum(nums=[i for i in range(1000)], target=3637))