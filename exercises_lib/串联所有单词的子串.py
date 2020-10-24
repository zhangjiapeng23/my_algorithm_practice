# 给定一个字符串 s 和一些长度相同的单词 words。
# 找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#  示例 1：
#  输入：
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#  示例 2：
#  输入：
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# 输出：[]
#  Related Topics 哈希表 双指针 字符串
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def match_substring(p: int, word: str) -> int:
            p_temp = p
            p_s = 0
            n = len(word)
            while p_s < n:
                if p_temp >= len(s):
                    return p
                if s[p_temp] == word[p_s]:
                    p_s += 1
                    p_temp += 1
                else:
                    return p
            else:
                return p_temp

        ans = []
        s_n = len(s)
        p_left = 0
        p_right = p_left
        while p_left < s_n:
            temp_words = words[:]
            while temp_words:
                for word in temp_words:
                    temp_p_right = match_substring(p_right, word)
                    if temp_p_right == p_right:
                        continue
                    else:
                        temp_words.remove(word)
                        p_right = temp_p_right
                        break
                else:
                    p_left += 1
                    p_right = p_left
                    break
            else:
                ans.append(p_left)
                p_left += 1
                p_right = p_left

        return ans



    def find_substring_hashmap(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n = len(s)
        p = 0
        word_l = len(words[0])
        word_n = len(words)
        words_hash = Counter(words)
        while p < n - word_l * word_n + 1:
            num = 0
            has_words_hash = {}
            while num < word_n:
                temp_word = s[p+num*word_l:p+(num+1)*word_l]
                if temp_word in words_hash:
                    if temp_word in has_words_hash:
                        has_words_hash[temp_word] += 1
                    else:
                        has_words_hash[temp_word] = 1
                    if has_words_hash[temp_word] > words_hash[temp_word]:
                        p += 1
                        break
                else:
                    p += 1
                    break
                num += 1
            else:
                ans.append(p)
                p += 1
        return ans

if __name__ == '__main__':
    s = 'ABCDCDAB'
    words = ['AB', 'CD', 'CD']
    test = Solution()
    res = test.findSubstring(s, words)
    res1 = test.find_substring_hashmap(s, words)
    print(res)
    print(res1)



