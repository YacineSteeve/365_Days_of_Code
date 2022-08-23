h, m = map(int, input().split())

if m >= 45:
    print(f'{h} {m-45}')
else:
    if h == 0:
        print(f'{23} {m+15}')
    else:
        print(f'{h-1} {m+15}')
