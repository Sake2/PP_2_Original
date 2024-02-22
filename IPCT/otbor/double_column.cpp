#include<iostream>
#include<numeric>
using namespace std;
int main(){
    int n,m,sum;
    cin >> n;
    long long int an[n];
    for (int i=0;i<n;++i){
        an[i] = 0;
        long long arr[11][11]={{0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0},
                               {0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0},
                               {0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0}};
        cin >> m;
        char a,b;
        for (int j=0;j<m;j++){
            cin >> a >> b;
            arr[int(a-97)][int(b-97)]++;
        }
        for (int k=0;k<11;++k){
            sum = arr[k][1]+arr[k][2]+arr[k][3]+arr[k][4]+arr[k][5]+arr[k][6]+arr[k][7]+arr[k][8]+arr[k][9]+arr[k][10];
            for (int l=0;l<10;l++){
                an[i] += sum * arr[k][l];
                sum -= arr[k][l+1];
            }
        }
        for (int k=0;k<11;++k){
            sum = arr[1][k]+arr[2][k]+arr[3][k]+arr[4][k]+arr[5][k]+arr[6][k]+arr[7][k]+arr[8][k]+arr[9][k]+arr[10][k];
            for (int l=0;l<10;l++){
                an[i] += sum * arr[l][k];
                sum -= arr[l+1][k];
            }
        }
    }
    for (int i=0;i<n;++i){
        cout << an[i] << endl;
    }
}