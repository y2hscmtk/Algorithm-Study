#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
int n,m,result = 0;
bool cantMix[201][201]; // 수의 범위가 작으므로 맵보다 배열이 유리
vector<int> selected;

/**
 * 같이 먹으면 안되는 아이스크림 조합 생성
 * 앞에서부터 아이스크림을 하나 고르고, 그 아이스크림과 함께 골라도 되는 경우만 세어서 3개 고를때까지 반복 => 숫자 세기
*/
// 몇개 골랐는지, 어떤 인덱스까지 탐색했는지(다음 인덱스부터 탐색)
void selectIce(int start){
    if(selected.size()==3){ // 3개를 골랐다면
        result++;
        return;
    }
    for(int i=start+1;i<n+1;i++){ // 1번부터 n번까지의 아이스크림에 대해
        // i번째 아이스크림을 현재 집합에 넣을 수 있는지 확인
        bool able = true; // 넣을 수 있음
        // 현재 집합에 포함된 수들과 합쳐서 넣어도 되는지 확인
        for(int j=0;j<selected.size();j++){
            if(cantMix[i][selected[j]]){ // i와 selected의 j번째 인덱스의 인자를 섞을 수 없다면
                able = false;
                break;
            }
        }
        if(able){ // 넣을수 있다면
            selected.push_back(i);
            selectIce(i);
            selected.pop_back();
        } 
    }
}


int main(){
    cin.tie(NULL) -> ios::sync_with_stdio(false);
    cin>>n>>m;
    int a,b;
    for(int i=0;i<m;i++){
        cin>>a>>b;
        // 섞어먹으면 안되는 조합들
        cantMix[a][b] = true;
        cantMix[b][a] = true;
    }
    selectIce(0); // 아이스크림 고르기
    cout<<result<<endl;
}