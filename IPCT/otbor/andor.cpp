#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
int findj( int max ){
    int i = 0;
    while ( pow(2,i) <= max and i <= 30 ){
        i++;
    }
    return pow(2,i-1);
}
int main() {
    int n;
    cin >> n;
    int arr[n],m,k;
    for (int i=0;i<n;++i){
        cin >> m >> k;
        int zxc[m],l=0;
        for (int j=0;j<m;++j){
            cin >> zxc[j];
        }
        sort(zxc,zxc+m);
        if ( k < m){
                for (int j = 0; j < k;j++){
                    zxc[j] = zxc[j] ^ findj(zxc[k]);
                }
        }
        else {
            for (int j = 0; j < k;j++){
                if (l+1 >= m){
                    l -= m;
                }
                l++;
                zxc[l] ^= int(pow(2,(30-j/m)));
            }
        }
        arr[i] = zxc[0];
        for(int j=1;j<m;++j){
            arr[i] = arr[i] & zxc[j] ;
        }
    }
    for (int i=0;i<n;++i){
        cout << arr[i] << endl;
    }
}