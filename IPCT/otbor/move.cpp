#include<iostream>
using namespace std;
bool aaaaa(char a[],char aa[],int h){
    int i=0;
    while(i<=h){
        if (a[i]!=aa[i]){
            return true;
        }
        i++;
    }
    return false;

}
int main() {
    int n;
    cin >> n;
    long long int arr[n];
    for (int i=0;i<n;++i){
        int m,c=0;
        cin >> m;
        char die[m+1],died[m+1],temp[m+1],a;
        for(int j=0;j<m;++j){
            cin >> a;
            die[j] = died[j] = temp[j] = a;
        }
        int ar[m];
        for (int j=0;j<m;++j){
            cin >> ar[j];
        }
        do
        {
            for(int j=0;j<m;++j){
                temp[j] = die[ar[j]];
            } 
            c++;
            for(int j=0;j<m;++j){
                die[j] = temp[j];
            } 

        }
        while (aaaaa(die,died,m) );
            arr[i] = c;
        
    }
    for(int i=0;i<n;++i){
        cout << arr[i] << endl;
    }
}