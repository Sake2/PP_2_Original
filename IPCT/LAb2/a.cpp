#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int perm(vector<int>vec,int n){ // [1,2]
    if (n == 1){
        for(int i=0;i<vec.size();++i){
            cout << vec[i] << " ";
        }
        cout << endl;
    }
    int fi = vec.size()-n;
    for(int i=fi;i<vec.size();++i){
        swap(vec[fi],vec[i]);
        perm(vec,n-1);
        swap(vec[fi],vec[i]);   
    }
    return 0;
}
int main (){
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int n;
    cin >> n;
    vector<int>vec;
    for (int i=0;i<n;++i)
    {
        vec.push_back(i+1);    
    }
    perm(vec,n);
    


}
