n, m = 4, 6
data = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]]

# 상하 반전
data = data[::-1]

# 좌우 반전
for i in range(n):
    data[i] = data[i][::-1]
