#include<iostream>
#include<algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;
    string ad[n];
    for (int i=0;i<n;++i){
        ad[i]="";
        int t,k;
        cin >> t >> k;
        int ar[t];
        char  arr[t+1],con;
        for (int j=0;j<t;j++){
            cin >> arr[j];
            ar[j] = 0;
        }
        int j=0,max,ss;
        while ( k - arr[j] + 97 >= 0 and j < t){
           ar[j] = arr[j] - 97; 
           j++; 
        }
        con = arr[j];
        max = *max_element(ar,ar+j);
        ss = k - max; 
        for (int h=0;h<t;h++){
            if (h==j){
                arr[h]=con;
            }
            else if (con - ss <= arr[h] and con >= arr[h]) {
                arr[h] = con-ss;
            }       
        }
        arr[j] -= ss;
        for (int h=0;h<t;++h){
            if (max+97 >= arr[h] and max != 0) {
                arr[h] = 'a';
            }  
            ad[i] += arr[h]; 
        }
        
    }
    for (int i=0;i<n;++i){
        cout << ad[i] << endl;
    }
}