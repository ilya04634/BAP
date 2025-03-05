import heapq

n = int(input())
operations = [input().split() for _ in range(n)]

heap = []
result = []
for op in operations:
    if op[0] == 'insert':
        x = int(op[1])
        heapq.heappush(heap, x)
        result.append(f'insert {x}')
    elif op[0] == 'getMin':
        x = int(op[1])
        while heap and heap[0] < x:
            result.append('removeMin')
            heapq.heappop(heap)
        if not heap or heap[0] != x:
            result.append(f'insert {x}')
            heapq.heappush(heap, x)
        result.append(f'getMin {x}')
    elif op[0] == 'removeMin':
        if not heap:
            result.append('insert 0')
            heapq.heappush(heap, 0)
        result.append('removeMin')
        heapq.heappop(heap)

print(len(result))
for line in result:
    print(line)