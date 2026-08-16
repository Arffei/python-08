n = int(input())
arr = list(map(int, input().split()))

result = [arr[-1]] + arr[:-1]
print(*result)