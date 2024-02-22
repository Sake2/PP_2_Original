#include<iostream>
using namespace std;
int main (){
    int n,m;
    cin >> n;
    string arr1[n];
    for (int i=0;i<n;++i){
        arr1[i] = "YES";
        cin >> m;
        char arr2[m];
        for (int j=0;j<m;++j){
            cin >> arr2[j];
        }
        int countB=0,countR=0;
        for(int j=0;j<m;++j){
            if (arr2[j] == 'W'){
                if ((countR == 0) != (countB == 0)){
                    arr1[i] = "NO";
                    break;
                }
                countB=countR=0;
            }
            else if (arr2[j] == 'R'){
                countR++;
            }
            else{
                countB++;
            }
            
        }
        if ((countR == 0) != (countB == 0)){
            arr1[i] = "NO";
        }
    }
    for(int i=0;i<n;++i){
        cout << arr1[i] << endl;
    }
}