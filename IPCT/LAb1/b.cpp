#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
int main() {
    int n,m=0;
    cin >> n;
    vector<int>vec[n];
    for (int i=0;i<n;++i){
        cin >> m;
        int k = log2(m);
        vec[i].push_back(m);
        if (k == log2(m)){
            continue;
        }
        if (m % 2 == 1 ){
            vec[i].push_back(m/2);
            vec[i].push_back(m/2+1);
            continue;
        }
        k=3;
        for(int k=3;k<=sqrt(m);k++){
            if (m%k==0){
                break;
            }
        }
        long long int sum = m/k+1+m/k;
        int up=m/k+1, down = m/k ;
        while (sum != m and down!=0){
            if (sum > m ){
                down--;
                sum = sum - up + down;
                up--;
                
            }
            else if (sum < m){
                down--;
                sum += down;
            }
        }
        if (down!=0){
        
        vec[i].push_back(down);
        vec[i].push_back(up);
        }
    }
    for (int i=0;i<n;++i){
        if (vec[i].size() == 1){
            cout << "IMPOSSIBLE" << endl;
        }
        else{
            cout << vec[i][0] << " = " << vec[i][1];
            for( int j=vec[i][1]+1;j<=vec[i][2];j++){
                cout << " + " << j;
             }
            cout << endl;
        }
    }
}