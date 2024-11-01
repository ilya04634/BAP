def mountainRanges(n, m, ls):
    ranges = [abs(ls[i]-ls[i-1])for i in range(n)]
    ranges.sort()

    return ranges[n-m-1]



n, m = map(int, input().split())
ls = list(map(int, input().split()))
result = mountainRanges(n, m, ls)
print(result)
