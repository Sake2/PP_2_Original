#include<iostream>
using namespace std;
int pow(int a, int n){
    if (n == 0){
        return 1;
    }
    else if (n%2 == 1) {
        return pow(a,n-1) *a;
    }
    else {
        return pow(a*a,n/2);
    }
}
int main (){
    string s[];
    getline >> 
    int a,b,c;
    cout << pow(a,b) % c << endl;
}