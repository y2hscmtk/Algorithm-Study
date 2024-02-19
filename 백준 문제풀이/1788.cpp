#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
// f(n) = f(n-1) + f(n-2)
// f(1) = f(0) + f(-1) 이므로, f(-1) = f(1) - f(0)
// f(n-2) = f(n)-f(n-1)
// N<=-1 일때
// f(N) = F(N-2) - F(N-1) 가 성립함
// 따라서 음수의 관점에서도 결국 평범한 피보나치 수열과 같은 흐름으로 수가 증가함
// 차이점은 짝수음수인 경우 -를 붙인다.
// f(0) = 0, f(-1) = 1, f(-2) = -1, f(-3) = 2, f(-4) = -3, f(-5) = 5 .. 

// 이 수가 충분히 커질 수 있으므로, 절댓값을 1,000,000,000으로 나눈 나머지를 출력한다
// => 저장할때부터 1,000,000,000로 나눈 나머지를 저장한다.
int main(){
    cin.tie(nullptr) -> ios::sync_with_stdio(false);
    int n;
    cin>>n;
    if(n<0){
        if(abs(n)%2==0)
            cout << -1; // 짝수 음수인 경우 -1 출력
        else
            cout << 1;
    }else if(n>0){ // 0이 아닌 양수인 경우
        cout << 1;
    }else{ // 0이면 0 출력
        cout << 0;
    }
    cout<<endl;
    n = abs(n);
    vector<int> dp(n+1);
    dp[0] = 0; // if n = 0;
    dp[1] = 1; // if n = 1;
    for(int i=2;i<n+1;i++){ // if n > 1;
        dp[i] = dp[i-1]%1000000000 + dp[i-2]%1000000000;
    }
    cout<<dp[n]%1000000000<<endl;
}