for _ in range(int(input())):
    _ = input()
    
    g, m = map(int, input().split())
    armies = {'Godzilla': list(map(int, input().split())),
              'MechaGodzilla': list(map(int, input().split()))}
    
    if max(armies['Godzilla']) >= max(armies['MechaGodzilla']):
        print('Godzilla')
    else:
        print('MechaGodzilla')