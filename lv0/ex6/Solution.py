# https://school.programmers.co.kr/learn/courses/30/lessons/340202?language=python3

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = usage * (100 + change[i]) / 100
        total_usage += usage
        if total_usage > storage:
            return i

    return -1