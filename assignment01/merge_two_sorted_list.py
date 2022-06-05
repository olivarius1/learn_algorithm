# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self,
                      list1: Optional[ListNode],
                      list2: Optional[ListNode]
                      ) -> Optional[ListNode]:
        """
        递归
        :param list1:
        :param list2:
        :return:
        """
        # 边界条件
        if not list1:
            return list2
        if not list2:
            return list1
        # 保留更小的头节点
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists2(self,
                       list1: Optional[ListNode],
                       list2: Optional[ListNode]
                       ) -> Optional[ListNode]:
        """
        迭代
        :param list1:
        :param list2:
        :return:
        """
        # 设置保护节点
        protect = ListNode()
        last = protect
        # last.next 指向小的，更新last
        while list1 and list2:
            # 第一次会修改protect节点
            if list1.val <= list2.val:
                last.next = list1
                list1 = list1.next
            else:
                last.next = list2
                list2 = list2.next
            last = last.next
        # 有一个迭代完，追加剩余
        last.next = list1 if list1 else list2
        return protect.next
