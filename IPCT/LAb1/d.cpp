#include<iostream>
using namespace std;
int main (){
    int n;
    cin >> n;
    int count = n/2 + n%2;
    for (int i=1;i<=n/2;++i){
        count += n/i;
    }
    cout << count;
}
