T = int(input()) # Number of test cases
for i in range(T):
    N, K = [int(s) for s in input().split(" ")]
    S = input()
    current_K = 0
    for j in range(N//2):
        if S[j] != S[N-1-j]:
            current_K += 1
    result = abs(current_K-K)
    print("Case #{}: {}".format(i+1, result))