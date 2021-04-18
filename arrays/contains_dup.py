
def contains_dups(nums):
    return len(set(nums)) != len(nums)

def contains_dups(nums):
    if len(nums) <= 1:
        return False
    s = sorted(nums)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return True
    return False


