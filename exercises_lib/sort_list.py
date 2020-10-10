from typing import List


class Solution:

    def bubble_sort(self, s: List) -> List:
        s_le = len(s)
        for i in range(s_le):
            for j in range(s_le-1-i):
                if s[j] > s[j+1]:
                    s[j], s[j+1] = s[j+1], s[j]
        return s

    def select_sort(self, s: List) -> List:
        s_le = len(s)
        for i in range(s_le):
            max_index = 0
            for j in range(s_le-i):
                if s[j] > s[max_index]:
                    max_index = j
            s[max_index], s[j] = s[j], s[max_index]
        return s

    def insert_sort(self, s: List) -> List:
        s_le = len(s)
        for i in range(s_le):
            temp = s[i]
            while i >= 0:
                if i == 0:
                    s[i] = temp
                    break
                elif s[i-1] >= temp:
                    s[i] = s[i-1]
                    i -= 1
                else:
                    s[i] = temp
                    break
        return s



if __name__ == '__main__':
    a = [5,1,0,12,-2,89,100,89,111,3,1,1]
    test = Solution()
    # ans1 = test.bubble_sort(a)
    # print(ans1)
    # ans2 = test.select_sort(a)
    # print(ans2)
    ans3 = test.insert_sort(a)
    print(ans3)



