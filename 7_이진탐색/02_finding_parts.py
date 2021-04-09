parts_stock_len = int(input())
parts_stock = list(map(int, input().split()))
parts_stock.sort()

req_stock_len = int(input())
req_stock = list(map(int, input().split()))

print("start")

result = []

for search_target in req_stock :
    start = 0
    end = req_stock_len - 1
    while start <= end :
        if parts_stock[(start + end) // 2] > search_target :
            end = (start + end) // 2
            continue
        elif parts_stock[(start + end) // 2] < search_target :
            start = (start + end) // 2
            continue
        elif parts_stock[(start + end) // 2] == search_target :
            result.append("yes")
            break