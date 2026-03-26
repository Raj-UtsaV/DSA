from Disjoint_set_union import DisjointSet
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisjointSet(n)
        
        email_to_index = {}
        for i in range(n):
            for email in accounts[i][1:]:
                if email not in email_to_index:
                    email_to_index[email] = i
                else:
                    ds.union_by_size(i,email_to_index[email])
                    
        merged_accounts = {}
        for email,index in email_to_index.items():
            parent_index = ds.find_ultimate_parent(index)
            if parent_index not in merged_accounts:
                merged_accounts[parent_index] = []
            merged_accounts[parent_index].append(email)
            
        result = []
        for index, emails in merged_accounts.items():
            name = accounts[index][0]
            emails.sort()
            result.append([name] + emails)
            
        return result

#
        