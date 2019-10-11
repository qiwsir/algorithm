"""
将一个整数，分拆为若干整数的和。例如实现：
4=4
4=3+1
4=2+2
4=2+1+1
4=1+1+1+1

所以divide(4) == 5

这里会将输出这样的分法有多少种。采用动态规划计算，提高速度
参考链接中的C++版本
https://github.com/Sean16SYSU/Algorithms4N/blob/master/Dynamic%20Programming/%E6%95%B4%E6%95%B0%E5%88%92%E5%88%86/Interger_dividence_dp.cpp
"""
def divide(n):
    arr = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        arr[i][i] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i < j:
                arr[i][j] = arr[i][i]
            elif i == j:
                arr[i][j] = 1 + arr[i][j-1]
            else:
                arr[i][j] = arr[i][j-1] + arr[i-j][j]
    return arr[n][n] 


if __name__=="__main__":
    print(divide(4))