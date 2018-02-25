from collections import deque

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # 이미 확인한 요소를 추적하기 위한 것
    searched = []
    # 큐에 요소가 있으면 계속 루프
    while search_queue:
        # 큐의 첫 번째 사람을 꺼냄
        person = search_queue.popleft()
        # 이전에 확인하지 않은 사람만 확인
        if person not in searched:
            # 망고 판매상인지 확인
            if person_is_seller(person):
                # 망고 판매상이 맞음
                print(person + ' 녀석이 사실 마피아 였던 거임!')
                return True
            else:
                # 망고 판매상이 아님
                # 모든 이웃을 탐색 목록에 추가
                search_queue += graph[person]
                # 이 요소를 확인한 것으로 표시
                searched.append(person)
    return False


def person_is_seller(name):
    # name의 마지막 문자가 m으로 끝나는지 확인
    # m으로 끝나면 망고판매상.
    return name[-1] == 'm'


search('you')
