#include<iostream>
using namespace std;
int main (){
    int n,x;
    string s[i];
    cin >> x >> n;
    bool f=false;
    long long int arr[3]={0,0,1};
    for(int i=0;i<n;++i){
        for (int j=0;j<3;++j){
            arr[j] *= x;
            if (arr[j] >= 10000000){
                arr[j-1] += arr[j] / 10000000;
                arr[j] %= 10000000;
            }
        }
    }
    for(int i=0;i<3;++i){
        s[i] = to_string(arr[i]);
    }
    for(int i=0;i<3;++i){
        for (int i=0;i<7-s[i].size();i++){
        }
}