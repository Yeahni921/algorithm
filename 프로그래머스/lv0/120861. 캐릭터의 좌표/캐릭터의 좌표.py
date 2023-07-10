def solution(keyinput, board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    keytype = ['right', 'left', 'down', 'up']
    x, y = 0, 0

    for key in keyinput:
        for j in range(4):
            if key == keytype[j]:
                nx = x + dx[j]
                ny = y + dy[j]
        if abs(nx) > board[0]//2 or abs(ny) > board[1]//2:
            continue
        x, y = nx, ny
    return [x,y]




