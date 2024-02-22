#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
int main (){
    int n,count=0;
    cin >> n;
    int arr[n-1],arr2[n-1];
    vector<int> vec;
    for (int i=2;i<=n;++i){
        arr2[i-2] = arr[i-2] = i;
    }
    for(int i=0;i<n-1;i++){
        for(int j=2;j<sqrt(n);j++){
            if  (arr[i] % j == 0){
                arr[i] = -1;
            }
        }
    }
    for(int i=0;i<n-1;++i){
        if (arr[i] !=1){
            vec.push_back(arr[i]);
        }
    }
    for (int i = 0;i<n-1;i++){
        for(int j=2;j<vec.size();j++){
            if (arr[i] % j == 0){
                int left = 0;
                int right = vec.size() -1 ;
                int middle  ;
                while (right - left != 1){
                    middle =(right - left)/2;
                    if ( j == vec[middle]){
                        count++;
                        break;
                    }
                    else if(j > vec[middle]){
                        left = middle;
                    }
                    else {
                        right = middle;
                    }
                }
            }
        }

    }
    cout << count;

}
