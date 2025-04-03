def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    res = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        commands = []
        for _ in range(n):
            ti = int(data[idx])
            xi = int(data[idx + 1])
            commands.append((ti, xi))
            idx += 2

        suc = 0
        cur_pos = 0
        tar_pos = 0
        start_time = 0
        end_time = 0

        for i in range(n):
            ti, xi = commands[i]
            next_ti = commands[i + 1][0] if i + 1 < n else float('inf')

            if start_time <= ti < end_time:
                dt = ti - start_time
                pos = cur_pos + dt * (1 if tar_pos > cur_pos else -1)

                if xi >= min(pos, tar_pos) and xi <= max(pos, tar_pos):
                    distance = abs(xi - pos)
                    arrival_time = ti + distance
                    if arrival_time <= next_ti:
                        suc += 1
            else:
                cur_pos = tar_pos if ti >= end_time else cur_pos + (ti - start_time) * (
                    1 if tar_pos > cur_pos else -1)
                tar_pos = xi
                start_time = ti
                end_time = ti + abs(tar_pos - cur_pos)

                if end_time <= next_ti:
                    suc += 1

        res.append(suc)

    print("\n".join(map(str, res)))


if __name__ == "__main__":
    main()