def maximalSquare(matrix):
    result, i, j = 0, 0, 0
    cache = matrix

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or j == 0:
                cache[i][j] = int(matrix[i][j])
                if cache[i][j] > result:
                    result = cache[i][j]
                continue
            if int(matrix[i][j]) > 0:
                cache[i][j] = 1 + min(cache[i][j - 1],
                                    cache[i - 1][j],
                                    cache[i - 1][j - 1])
            else:
                cache[i][j] = 0
            if cache[i][j] > result:
                result = cache[i][j]
    return result * result


print(maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
              "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
)