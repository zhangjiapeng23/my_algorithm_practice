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

    def merge_sort(self, low: int, high: int, s: List):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid, s)
            self.merge_sort(mid+1, high, s)
            self.merge(low, mid, high, s)

    def merge(self, low: int, mid: int, high: int, s: List):
        i = low
        j = mid + 1
        sort_s = []
        while i <= mid and j <= high:
            if s[i] <= s[j]:
                sort_s.append(s[i])
                i += 1
            else:
                sort_s.append(s[j])
                j += 1
        if i <= mid:
            sort_s.extend(s[i:mid+1])
        else:
            sort_s.extend(s[j:high+1])
        s[low:high+1] = sort_s






if __name__ == '__main__':
    a = [5,1,0,12,-2,89,100,89,111,3,1,1]
    # test = Solution()
    # # ans1 = test.bubble_sort(a)
    # # print(ans1)
    # # ans2 = test.select_sort(a)
    # # print(ans2)
    # ans3 = test.insert_sort(a)
    # print(ans3)

    test = Solution()
    test.merge_sort(0, len(a)-1, a)
    print(a)

    # test.merge_sort(0, len(a)-1, a)
    # print(a)



