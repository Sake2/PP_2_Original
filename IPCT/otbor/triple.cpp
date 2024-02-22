#include<iostream>
#include<algorithm>
using namespace std;
int main (){
    int n,m,count;
    cin >> n;
    int arr[n];
    for (int i=0;i<n;++i){
        arr[i] = -1;
        count = 0;
        cin >> m;
        int arr2[m];
        for(int j=0;j<m;++j){
            cin >> arr2[j];
        }
        sort(arr2,arr2+m);
        for (int j=m-1;j>=0;--j){
            if (count == 2){
                    arr[i] = arr2[j];
                    break;
                }
            else if (arr2[j]!=arr2[j-1]){
                count = 0;
            }
            else{
                count++ ;
                
            }
        }
    }
    for(int i=0;i<n;++i){
        cout << arr[i] << endl;
    }
}