# 오픈채팅방 https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dic = {}

    for i in record:
        sp = i.split()
        if len(sp) == 3:
            dic[sp[1]] = sp[2]

    for i in record:
        sp = i.split()
        if sp[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dic[sp[1]])
        elif sp[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dic[sp[1]])
    return answer

