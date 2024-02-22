#include<iostream>
#include<cmath>
#include<vector>
using namespace std;
int fact(int n){
    int cou=1;
    for(int i=2;i<=n;++i){
        cou *=i;
    }
    return cou;
}
int main (){
    long long int n;
    int count=0,fac;
    vector<int>vec;
    cin >> n;
    for(int i=2;i<=sqrt(n);++i){
        if (n%2==0){
            fac = 0;
        while(n%i == 0){
            n /= i;
            count ++;
            fac++;
        }
        vec.push_back(fac);
        }
    }
    count=fact(count);
    for(int i=0;i<vec.size();++i){
        count /= fact(vec[i]);
    }
    cout << count;
}