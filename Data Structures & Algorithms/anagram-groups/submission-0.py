class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str in strs:
            key = "".join(sorted(str))

            if key not in groups:
                groups[key] = []
            
            groups[key].append(str)

        final_list = []

        for key in groups:
            final_list.append(groups[key])

        return final_list
