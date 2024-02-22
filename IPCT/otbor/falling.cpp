#include<iostream>
using namespace std;
int main(){
    int n,m,v;
    cin >> n;
    for (int i=0;i<n;++i){
        cin >> m >> v;
        char arr[m][v];
        int countr = 0;
        for (int j=0;j<m;++j){
            for (int k=0;k<v;k++){
                cin >> arr[j][k];
            }
        }
        for (int j=0;j<v;++j){
            for (int k=0;k<m;k++){
                if ( arr[k][j] == '*'){
                    countr++;
                }
                else if ( arr[k][j] == '.'){
                    arr[k][j] = '*';
                    arr[k-countr][j] = '.';
                }
                else{
                    countr = 0;
                }
            }
            countr = 0;
        }
        for (int j=0;j<m;++j){
            for (int k=0;k<v;k++){
                cout << arr[j][k];
            }
            cout << endl;
        }
    }
}