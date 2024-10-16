from typing import List
def twoSum(nums: List[int], target : int) -> List[int]:
    ret_Pair=[]

    twoNums=[[[first_val, fisrt_idx], [second_val, second_idx]]
    for fisrt_idx, first_val in enumerate(nums)
    for second_idx, second_val in enumerate(nums) if fisrt_idx<second_idx]
    '''twoNums( [ pair1, index_of_pair1 ], [ pair2, index_of_pair2 ] )'''
    for pair in twoNums:
        Sum_of_pair=pair[0][0]+pair[1][0]
        '''Sum_of_pair=pair1+pair2'''
        if(Sum_of_pair==target):
            '''if Sum_of_pair == target 
            then append index of 2 pair in return_Pair'''
            ret_Pair.append(pair[0][1])
            ret_Pair.append(pair[1][1])
    return ret_Pair