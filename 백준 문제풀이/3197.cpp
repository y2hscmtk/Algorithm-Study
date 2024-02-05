#include <bits/stdc++.h>
using namespace std;
int r,c,day = 0; // 0부터 날짜 시작
vector<string> graph;
bool visited[1501][1501];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
vector<pair<int,int> > goose; // 거위 위치 저장용
/**
 * 예상 알고리즘 : 시뮬레이션, 구현, BFS
 * '.'은 물, 'x'는 얼음
 * 1. 만날 수 있는지 확인한다. (bfs)
 * 2. 만날 수 없었다면 얼음을 지운다. (bfs)
 * 3. 1으로 돌아간다.
*/

// 얼음 녹이기
void meltIce(int s, int e){
    queue<pair<int,int> > q; //(int,int)를 저장할 수 있는 큐 생성
    q.push(make_pair(s,e)); // 탐색 시작 좌표
    visited[s][e] = true;
    // 큐가 비어있지 않은 동안 반복
    while(!q.empty()){
        pair<int,int> p = q.front(); q.pop();
        int x = p.first;
        int y = p.second;
        // 현재 위치에서 상하좌우 검사하여 방문하지 않은 .에 대해서 방문처리하고 큐에 삽입
        // X를 만나면 .으로 변환후 방문처리(큐에 넣지는 않음)
        int nx,ny;
        for(int i=0;i<4;i++){
            nx = x + dx[i];
            ny = y + dy[i];
            if (0 <= nx && nx < r && 0 <= ny && ny < c) {
                if(!visited[nx][ny]){
                    // 백조와 만났을때는 어떻게 처리?
                    if(graph[nx][ny] == '.')
                        q.push(make_pair(nx,ny));
                    else if(graph[nx][ny] == 'X'){
                        graph[nx][ny] = '.'; // 녹인다.
                    }
                    visited[nx][ny] = true; //'.','#','L' 모두 방문처리 하는것은 확정
                }
            }
        }
        
    }
}


// 만났는지 안만났는지 확인
bool isMeet(){
    fill(&visited[0][0],&visited[r][c],false);
    queue<pair<int,int> > q;
    pair<int,int> start = goose[0]; // 시작 위치
    pair<int,int> dest = goose[1]; // 도착지
    int s = start.first, e = start.second;
    int ds = dest.first, de = dest.second;

    visited[s][e] = true;
    q.push(make_pair(s,e));
    while(!q.empty()){
        pair<int,int> p = q.front(); q.pop();
        int x = p.first;
        int y = p.second;
        // 목적지에 도달하였다면
        if(x==ds&&y==de)
            return true;
        for(int i=0;i<4;i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0<=nx&&nx<r&&0<=ny&&ny<c){
                // 방문하지 않은 지역중에 벽이 아닌 지형을 마주한다면
                if((!visited[nx][ny]) && graph[nx][ny]!='X'){
                    visited[nx][ny] = true; // 방문처리하고
                    q.push(make_pair(nx,ny)); // 큐에 삽입
                }
            }
        }
    }
    return false;
}


int main(){
    cin.tie(NULL) -> ios::sync_with_stdio(false);
    cin>>r>>c;
    string s;
    // 가장 빠른 시점에 두 L의 위치를 저장해야 할듯?
    for(int i=0;i<r;i++){
        cin.ignore();
        cin >> s;
        graph.push_back(s);
        // 거위의 위치 저장
        for(int j=0;j<c;j++){
            if(s[j] == 'L'){
                goose.push_back(make_pair(i,j));
                break;
            }
        }
    }
    // 만날 수 있을때까지 시뮬레이션
    while(true){
        // 만났는지 확인
        if(isMeet()){
            cout<<day<<endl;
            return 0;
        }
        // visited 배열 초기화
        fill(&visited[0][0],&visited[r][c],false);
        // 얼음 녹이기
        for(int i=0;i<r;i++){
            for (int j = 0; j < c; j++){
                // 아직 방문한적 없는 물을 만났을때
                if(!visited[i][j] && graph[i][j] == '.')
                    meltIce(i,j); // 인접한 물 녹이기 시작
            }
        }
        // // 현재 상태 출력(확인용)
        // for(auto &s : graph){
        //     for(auto &a : s){
        //         cout<<a;
        //     }
        //     cout<<endl;
        // }
        day++;
    }
}