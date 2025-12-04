N = int(input())  # N을 입력받음

for i in range(1, N + 1):
    # 공백의 개수는 N - i, 별의 개수는 i
    print(" " * (N - i) + "*" * i)
