#include <iostream>
#include <vector>
using namespace std;

void swap(int &a, int &b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
int main()
{
    int n;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int t;
        cin >> t;
        v.push_back(t);
    }
    // 정렬 시작
    for (int i = 0; i < v.size(); i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (v[i] < v[j])
                swap(v[i], v[j]);
        }
    }

    // 출력
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }
}