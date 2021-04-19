
def intersect(nums1, nums2):
    return set.intersection(set(nums1), set(nums2))

def intersect(nums1, nums2):
    """
    two pointer solution
    i corresponds to nums1 index
    j corresponds to nums2 index
    if nums1[i] > nums2[j], then j+=1
    elif nums1[i] < nums2[j], then i+=1
    else: it's an intersection, increment both i and j
    """
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)


    results = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            if nums1[i] not in results:
                results.append(nums1[i])
            i += 1
            j += 1
    return results


def intersect(nums1, nums2):
    '''
    This is a Facebook interview question.
    They ask for the intersection, which has a trivial solution using a hash or a set.

    Then they ask you to solve it under these constraints:
    O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
    You are told the lists are sorted.
    '''
    pass


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    nums2 = [0, 2, 3]
    res = intersect(nums1, nums2)
    print(f'\nres: {res}')
