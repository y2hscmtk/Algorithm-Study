#include <bits/stdc++.h>
using namespace std;
int board[101][101];
int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};
int result = 0;
/**
 * 전체 도화지는 100*100 크기
 * 색종이는 10*10
 * 색종이가 도화지 밖으로 나가는 경우는 없다
 * 검은색 영역 구하기
 * 
*/

// 검은색 영역으로 칠하기
void draw(int s,int e){
    for(int i=s;i<s+10;i++){
        for(int j=e;j<e+10;j++){
            board[i][j] = 1;
        }
    }
    
}

// 자신이 0이고, 상,하,좌,우 중 하나에 1이 존재한다면 테두리
void count(){
    for(int i=0;i<101;i++){
        for(int j=0;j<101;j++){
            if(board[i][j]!=1)
                continue;
            bool isOne = false;
            for(int k=0;k<4;k++){
                int ni = i + dx[k];
                int nj = j + dy[k];
                if(0<=ni&&ni<=100&&0<=nj&&nj<=100){
                    // 1이 존재하는지 확인
                    if(board[ni][nj] == 1){
                        isOne = true;
                        break;
                    }
                }
            }
            if(isOne)
                result++;
        }
    }
}

int main(){
    int t,s,e; cin>>t;
    while(t--){
        cin>>s>>e;
        draw(s,e);
    }

    for(int i =0;i<101;i++){
        for(int j=0;j<101;j++){
            cout<<board[i][j];
        }
        cout<<endl;
    }
    count();
    cout<<result;
    
}