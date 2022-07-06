import sys
input = sys.stdin.readline

K = int(input())

dq = []
for _ in range(K):
    cmd = input().split()
    if len(cmd) == 2:
        if cmd[0] == "push_back":
            dq.append(int(cmd[1]))
        elif cmd[0] == "push_front":
            dq.insert(0, int(cmd[1]))
    elif cmd[0] == "pop_front":
        if dq:
            print(dq.pop(0))
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(dq))
    elif cmd[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)