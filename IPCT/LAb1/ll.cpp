#include<iostream>
#include<vector>
using namespace std;
int main (){
    vector<int> vec;
    int y=1,count=1;
    while(y!=0){
        cin >> y;
        if (y == 0){
            break;
        }
        vec.push_back(y);
    }
    for (int i=0;i<vec.size();++i){
        for(int j=2;j<vec[i];j++){
            if( (vec[i] % (vec[i] % j)) != 0 and vec[i] % j !=0){
                count ++;
            }
        }
        vec[i] =count;
        count=1;
    }
    for(int i=0;i<vec.size();i++){
        cout << vec[i] << endl;
    }
}