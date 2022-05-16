# < RGB거리 >
# 1 ~ N번 집까지 빨, 초, 파 중 하나로 색칠 -> 칠하는 비용이 주어짐.
# - 1번 집의 색은 2번집의 색과 같지 않아야함.
# - N번집의 색은 N-1번 집의 색과 같지 않아야 함.
# - i ( 2 <= i <= N-1 )번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야함.
# 최솟값 구하기
# 문제유형 : DP
# 자료구조 : 2차원 리스트  - 모든 경우의 비용 값을 들고가기 위해서
# < 동작 순서 >
# 1. 먼저 1 ~ N번 까지의 집을 표현하기 위한 리스트 하나를 만들어줌
#    이는 색칠의 비용값을 저장하기 위함.
# 2. 위에서 본 규칙에 따르면 1번 2번의 색은 달라야하고 2번 3번 색은 달라야하고
#    1번 3번의 색은 같아도 괜찮음. 그말은 n-1, n 사이의 관계만 생각하면 된다는 뜻임.
# 3. 그래서 2번부터 N번까지 돌리면서 이전 비용의 합 더하기 현재 비용중 이전과 다른 색깔의
#    비용 중 적은 것 -> min()을 이용하여 표현하면 좋을 듯.
# 4. 반복문이 끝나고 N번째 인덱스를 출력
# < 아이디어 >
# - 1 2 3 번째가 있다면 1 - 2, 2 - 3 이렇게 연관이 있기때문에 1, 2를 결정해도 3에서 2를
#   바꿔야하는 경우가 생김.
# - 그 경우는 3의 최소값이 2보다 더 이득인 경우임. 그럼 이득인지는 어떻게 알 수 있음?
# - 2의 최소값 + 3의 두번째 최소값 > 2의 두번째 최소값 + 3의 최소값 이면 된다.
# - 1의 최소값을 넣어놓고 2, 3을 보면서 최종 2를 결정.
# - 그리고 3과 4를 보면서 최종 3을 결정.
# 3
# 1 2 3
# 1 2 3
# 100 1 100
# 이 케이스를 통과못함.
# < 다른 아이디어 >
# 하나로 고정하는게 아니라 모든 경우를 전부 다 들고가는 형태로 짜자.
# 여기서 중요한 것은 결국 현재 비용 + 이전 비용했을 때 최소가 되야하는 건데
# 하나로 고정해서 가면 바뀌어서 다시 이전으로 돌아가야하는 경우가 생기는데 그럴꺼면
# 그냥 백트래킹 쓰지.
# 그니까 전부 다 들고가고 그 중 최소값을 출력하면 됨.
def solution():
    sumCost = [[0]*(3) for _ in range(n)]
    sumCost[0][0] = cost[0][0]
    sumCost[0][1] = cost[0][1]
    sumCost[0][2] = cost[0][2]
    for i in range(1, n):
        sumCost[i][0] = min(sumCost[i-1][1] + cost[i][0], sumCost[i-1][2] + cost[i][0])
        sumCost[i][1] = min(sumCost[i - 1][0] + cost[i][1], sumCost[i - 1][2] + cost[i][1])
        sumCost[i][2] = min(sumCost[i - 1][0] + cost[i][2], sumCost[i - 1][1] + cost[i][2])
    return min(sumCost[n-1])
if __name__ == "__main__":
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    # 0 ~ n-1
    print(solution())