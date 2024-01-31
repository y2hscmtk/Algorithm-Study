//
// Created by Choi76 on 2024/01/31.
//
#include <iostream>
#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
/**
 * 가르침
 * k개의 '글자'를 배움
 * k개의 글자를 알고 있다고 가정할때 단어를 읽을 수 있는지 없는지 파악
 * a,c,i,n,t 는 "anta", "tica" 로 인해 무조건 알아야 하는 단어
 * k가 만약 5미만이라면 어떠한 단어도 읽을 수 없다.(anta + ? + tica 이므로)
 * 각 단어별로 k개를 선택한 후(백 트래킹) 해당 단어 리스트로 읽을 수 있는 단어인지 파악
 * => 그 단어들을 알고 있는 시점에 몇개의 단어를 읽을수 있는지 비교
 * */
int result = 0; // 읽을 수 있는 최대 단어의 개수
vector<string> words;

int countWords(vector<bool> &v){
    int count = 0;
    // 현재 알고있는 단어들로 단어를 읽을 수 있는지 없는지 확인
    for (auto &word: words) {
        //cout<<"target : " << word <<endl;
        bool canRead = true; // 읽을 수 있다.
        for (auto &w: word) {
            //cout<<w<<" ";
            if(!v[w-'a']){ // 단어가 없다면
                canRead = false; // 읽을 수 없다.
                break;
            }
        }
        // 읽을 수 있다면 count++;
        if(canRead)
            count++;
    }
    return count;
}

// v는 해당 단어를 알고 있는지 없는지 확인 하기 위함
void teachWord(int start,int count,int k,vector<bool>& v) {
    if(count == k-5){
        // 현재 알고 있는 글자들로 몇개의 단어를 읽을 수 있는지 확인
        // result 갱신
        result = max(result,countWords(v));
        return;
    }
    // k-5개의 단어를 선택
    for(int i=start;i<26;i++){
        // 현재 인덱스의 글자를 선택하지 않은 경우에 대해서만
        if(v[i])
            continue;
        // 백트래킹
        v[i] = true;
        teachWord(i+1,count+1,k,v);
        v[i] = false;
    }
}

int main(){
    cin.tie(nullptr)->ios::sync_with_stdio(false);
    int n,k;
    cin>>n>>k;
    for (int i = 0; i < n; i++) {
        string w; cin >> w;
        words.push_back(w);
    }
    if(k<5)
        cout<<0; // 5개 미만을 가르칠 수 있다면 어떠한 단어도 못 읽는다.
    else{
        vector<bool> v(26, false);
        // a,c,i,n,t 는 이미 가르쳤다고 가정
        v['a'-'a'] = true;
        v['c'-'a'] = true;
        v['i'-'a'] = true;
        v['n'-'a'] = true;
        v['t'-'a'] = true;

        teachWord(0,0,k,v); // 어떤 단어를 가르칠 것인지 백트래킹

        cout<<result;
    }
    return 0;
}


