# https://www.acmicpc.net/problem/12865
'''
문제
이 문제는 아주 평범한 배낭에 관한 문제이다.

한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 

세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 
해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 

아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 

준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 

두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.
'''
# 참고한 사이트
# 이론참고
# https://gsmesie692.tistory.com/113
# https://jeonyeohun.tistory.com/86
'''
이론 정리

최대 가치를 갖는것이 목표이기때문에, 0kg부터 k kg까지 가방의 최대 무게를 달리하며 해당 시점에서 가방에 넣을수 있는 최대 가치를 구한다.
가방에 물건을 넣는 경우는 물건을 넣을때와 넣지 않을때 두 가지 경우로 나뉘는데,

가방에 i번째 물건을 넣는다고 가정할때, 
i번째 물건의 무게가 가방의 최대 무게를 넘지 않을때와 넘을때로 경우가 갈린다.
i번째 물건의 무게가 가방의 최대 무게를 넘을때는, 
i번째 물건을 넣지 않은 경우에서의 최대가치가 해당 시점에서의 최대가치가 되고,
i번째 물건의 무게가 가방의 최대 무게를 넘지 않을때는,
i번째 물건의 무게만큼 가방의 무게를 비워두고 i번째 물건의 가치를 더한 값과, i번째 물건을 넣지 않은 지금까지의 최대 가치중 비교하여
더 큰 값을 해당 시점에서의 최대가치로 삼으면 된다.
'''
