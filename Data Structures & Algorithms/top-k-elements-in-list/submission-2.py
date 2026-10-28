class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        freq_elem = []
        for x in nums:
            dict[x] = dict.get(x, 0)+1
            # if dict[x] == k:
            #     freq_elem.append(x)
        # print(dict)
        dict_sorted = sorted(dict.items(), key=lambda x:x[1], reverse=True)
        # print(dict.items())
        # print(dict_sorted)
        freq_elem = [item[0] for item in dict_sorted[:k]]
        # print(freq_elem)
        return freq_elem
        