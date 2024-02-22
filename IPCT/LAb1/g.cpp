#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
#include<iterator>
using namespace std;
int main(){
    int n;
    cin >> n;
    vector<int>vec[n];
    for(int j=0;j<n;++j){
    int a,b;
    cin >> a >> b;
    vec[j].resize(a,b);
    fill(vec[j].begin(),vec[j].end(),1);
    for (int i=2;i<=sqrt(b);i++){
        for(int l=0;l<=b;l++){
            if((l+a) % i == 0 and (l+a) > i){
                vec[j][l]--;
                }
        }
    }}
    for(int j=0;j<n;++j){
        int count =0;
        for(int k=0;k<=vec[j].size();k++){
            if (!vec[j][k]){
            count++;
            }
        }
        cout << count << endl;
    }
}