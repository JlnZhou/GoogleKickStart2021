T = int(input()) # Number of test cases
for case in range(T):
    N = int(input())
    S = input()
    y = [1]
    for i in range(1, N):
        if S[i] > S[i-1]:
            y.append(y[i-1] + 1)
        else:
            y.append(1)
    res = ""
    for yi in y:
        res += " " + str(yi)
    print("Case #{}:{}".format(case+1, res))