from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = {}
        for _domain in cpdomains:
            _num, domain = _domain.split(' ')
            domain_split = domain.split('.')
            for i in range(len(domain_split)):
                a_domain = '.'.join(domain_split[i:])
                if a_domain in ans:
                    ans[a_domain] += int(_num)
                else:
                    ans[a_domain] = int(_num)
        return [f"{v} {k}" for k, v in ans.items()]
