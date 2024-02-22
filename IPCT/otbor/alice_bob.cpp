 #include<iostream>
#include<numeric>
using namespace std;
int main() {
    int n;
    cin >> n;
    int an[n],m;
    for (int i=0;i<n;++i){
        cin >> m;
        int arr[m],A=0,B=0,j1=0,j2=m-1,sum,s=0;
        for(int j=0;j<m;j++){
            cin >> arr[j];
        }
        while ( j1-1<= j2 ){
            if ( A < B ){
                A += arr[j1];
                j1++;
                s++;
            }
            else if ( A > B ){
                B += arr[j2];
                j2--;
                s++;
            }
            else {
                sum = s;
                A += arr[j1];
                j1++;
                s++;
            }
        }
        an[i] = sum;
    }
    for (int i=0;i<n;++i){
        cout << an[i] << endl;
    }
}