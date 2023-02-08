with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
    f_out.write(f'{sum(map(int, f_in.read().split()))}')
