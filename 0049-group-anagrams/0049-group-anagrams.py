class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        d = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            d[key].append(i)
        return d.values()
        