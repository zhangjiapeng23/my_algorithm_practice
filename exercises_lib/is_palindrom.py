# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
#  示例 1:
#  输入: 121
# 输出: true
#
#  示例 2:
#  输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#  示例 3:
#  输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#  进阶: 
#  你能不将整数转为字符串来解决这个问题吗？


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        if str_x[::-1] == str_x[:]:
            return True
        else:
            return False

    def isPalindrome_nostr(self, x: int) -> bool:
        if x < 0:
            return False
        elif x != 0 and x % 10 == 0:
            return False
        else:
            reverse_num = 0
            while x > reverse_num:
                reverse_num = reverse_num * 10 + x % 10
                x //= 10
            # 如果x的长度是奇数，revers_num的结果应该去掉最后一位的中位数后进行比较。
            return x == reverse_num or x == reverse_num // 10


if __name__ == "__main__":
    a = 1221
    test = Solution()
    ans = test.isPalindrome_nostr(a)
    print(ans)

