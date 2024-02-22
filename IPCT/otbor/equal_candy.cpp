#include<iostream>
#include<algorithm>
using namespace std;
int main (){
    int n,m,count,*min;
    cin >> n;
    int arr2[n];
    for (int i=0;i<n;++i){
        count=0;
        cin >> m;
        int arr[m];
        for (int j=0;j<m;j++){
            cin >> arr[j];
        }
        min=min_element(arr,arr+m);
        for (int j=0;j<m;j++){
            count+=arr[j]-*min;
        }
        arr2[i]=count;
        count=0;
    }
    for (int i=0;i<n;++i){
        cout << arr2[i] << endl;
    }
}