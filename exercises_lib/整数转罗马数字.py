"""
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，
例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

"""
class Solution:

    def intToRoman(self, num: int) -> str:
        roman_map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }
        ans = ''
        array = 0
        while num > 0:
            _num = num % 10
            _num_array = pow(10, array)
            temp_num = _num * _num_array
            if temp_num < 4 * _num_array:
                ans = roman_map[_num_array]*_num + ans
            elif temp_num == 4 * _num_array:
                ans = roman_map[_num_array] + roman_map[5*_num_array] + ans
            elif temp_num == 5 * _num_array:
                ans = roman_map[5*_num_array] + ans
            elif temp_num < 9 * _num_array:
                ans = roman_map[5*_num_array] + roman_map[_num_array] * ((temp_num-5*_num_array)//_num_array) + ans
            elif temp_num == 9 * _num_array:
                ans = roman_map[_num_array] + roman_map[_num_array*10] + ans
            num //= 10
            array += 1
        return ans

    def int_to_roman(self, num: int) -> str:
        # 贪心算法，从数字的最高位开始匹配， 每次找到符合当前数最大的符号
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                  (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        ans = ''
        for _num, symbol in digits:
            if num == 0: break
            count, num = divmod(num, _num)
            ans += symbol * count
        return ans


if __name__ == '__main__':
    num = 202
    test = Solution()
    res = test.int_to_roman(num)
    res1 = test.intToRoman(num)
    print(res, "\n" + res1)
