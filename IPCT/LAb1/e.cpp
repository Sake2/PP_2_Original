#include<iostream>
#include<vector>
#include<math.h>
#include<iterator>
using namespace std;
int main(){
    int a,b;
    cin >> a >> b;
    vector<int>vec;
    if (a == 1){
        a =2;
    }
    for(int i=a;i<=b;i++){
        vec.push_back(i);
    }
    for (int i=2;i<=sqrt(b);i++){
        for(vector<int>::iterator it=vec.begin();it<vec.end();++it)
            if(*it % i == 0 and *it > i){
                vec.erase(it);
                }
        }
    
    for(int x : vec){
        cout << x << " ";
    }
}