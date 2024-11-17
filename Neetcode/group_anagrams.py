from typing import List
import json

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        groups = {}
        for id,s in enumerate(strs):
            info = {}
            info['length'] = len(s)
            char_map = {}
            hash_sum = 0
            for letter in s:
                hash_sum+=ord(letter)
                if char_map.get(letter)== None:
                    char_map[letter] = 1
                else:
                    char_map[letter]+=1
                
            info['char_map'] = char_map
            info['grouped'] = 0
            info['hash_sum'] = hash_sum
            info['str_value'] = s
            table[id] = info
        
        for id in table:            
            if table[id]['grouped'] == 1:
                break
            string_grouped = 0
            for leader_id in groups:
                match = 0

                if table[id]['length'] == table[leader_id]['length'] and \
                    table[id]['hash_sum'] == table[leader_id]['hash_sum']:
                    match = 1
                    char_map_s = table[id]['char_map']
                    char_map_leader = table[leader_id]['char_map']
                    for letter in char_map_s:
                        if char_map_s[letter] != char_map_leader.get(letter,0):
                            match = 0
                            break
                if match == 1:
                    groups.get(leader_id).append(table[id]['str_value'])
                    table[id]['grouped'] == 1
                    string_grouped = 1
                    break
            if string_grouped == 0:
                groups[id] = [table[id]['str_value']]
        result = [groups[s] for s in groups]
        return result

result_1 = Solution()
op = result_1.groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])
print(op)
print(json.dumps(op,indent=4))