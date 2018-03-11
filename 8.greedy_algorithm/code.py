# 배열 넣으면 집합이 된다.
# set을 사용하여 중복된 원소를 가지지 않는다.
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 방송국 목록
stations = dict()
stations["kone"] = set(['id', 'nv', 'ut'])
stations["ktwo"] = set(['wa', 'id', 'mt'])
stations["kthree"] = set(['or', 'nv', 'ca'])
stations["kfour"] = set(['nv', 'ut'])
stations["kfive"] = set(['ca', 'az'])

# 방문한 방송국의 목록을 저장할 집합
final_stations = set()

# 모든 방송국을 다 돌때 까지
while states_needed:
    # 아직 방송이 되지 않는 주 중에서 가장 많은 주를 커버하고 있는 방송국
    best_station = None
    # 아직 방송이  되지 않은 주 중에서 해당 방송국이 커버하는 주의 집합
    states_covered = set()

    # 모든 방송국 중에 어떤 것이 최선의 선택인지 알아봄.
    for station, states_for_station in stations.items():
        # 교집합
        # states_needed와 states_for_station에 모둠 포함된 주의 집합.
        # 아직 방송되지 않는 주 중에서 현재 고려하고 있는 방송국이 커버하는 주의 집합.
        covered = states_needed & states_for_station
        # 현재의 bset_station보다 더 많은 주를 커버 하는지 확인
        if len(covered) > len(states_covered):
            # 그렇다면 이 방송국이 새로운 best_station
            best_station = station
            # 방송국이 커버 하는 주의 집합을 갱신
            states_covered = covered

    # 이 방송국에서 커버하는 주는 이제 더이상 고려할 필요가 없다.
    states_needed -= states_covered
    # 최선의 선택을 받은 방송국을 목록에 추가
    final_stations.add(best_station)

print(final_stations)