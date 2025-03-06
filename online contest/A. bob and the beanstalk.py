def main(n, k, ls):
    bs_length = 0
    bob_meters = 0
    for i in range(n):
        bs_length += ls[i]
        bob_bs_dif = bs_length - bob_meters
        if bob_bs_dif < k:
            bob_meters += bob_bs_dif
        else:
            bob_meters+=k

    dif = bs_length - bob_meters
    if dif % k != 0:
        time_of_climbing = dif//k+1+n
    else:
        time_of_climbing = dif//k+n
    return time_of_climbing


n, k = map(int, input().split())
ls = list(map(int, input().split()))
print(main(n, k, ls))

