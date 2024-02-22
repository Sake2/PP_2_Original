#include<iostream>
#include<vector>
#include<utility>
#include<cmath>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<pair<int, int> > vec;
    for (int i=2; i <= sqrt(n); i++){
        if ( n%i == 0){
            int pow = 0;
            while( n%i == 0 ){
                n /= i;
                pow++;
            }
            vec.push_back(make_pair(i, pow));
        }
    }
    if (n!=1){
    vec.push_back(make_pair( n, 1 ));
    }
    for(int i=0;i<=vec.size()-1;i++){
        cout << vec[i].first ;
        if (vec[i].second != 1) {
            cout << "^" << vec[i].second ;
        }
        if (i != vec.size()-1){
            cout << "*";
        }
    }
}