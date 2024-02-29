class Solution:
    def AllPossibleStrings(self, s):
        ret, n = [], len(s)
        def collect(i, sofar=""):
            nonlocal ret, n, s
            if sofar:
                ret.append(sofar)
            if i >= n:
                return
            for k in range(i, n):
                collect(k+1, sofar+s[k])
        collect(0)
        return sorted(ret)