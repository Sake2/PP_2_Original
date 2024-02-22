#include<iostream>
#include<vector>
#include<utility>
using namespace std;
int main(){
    int n;
    cin >> n;
    vector<pair<int,int> > vec;
    for(int i=0;i<n;++i){
        int x=1,a,b,y;
        cin >> a >> b;
        if (a%2==0 and b%2==0){
            vec.push_back(make_pair(0,0));
            continue;
        }
        while(true){
            if ((a*x-1) % b == 0){
               
                y= (a*x-1) / b;
                vec.push_back(make_pair(x,y));
                break;
            } 
            x++;
        }
    }
    for(int i=0;i<n;++i){
        if(vec[i].first == 0){
            cout << "NO SOLUTION" << endl;
        }
        else {
            cout << vec[i].first << " -" << vec[i].second << endl;
        }
    }
}