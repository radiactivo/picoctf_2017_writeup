#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    string str="tu1|\\h+&g\\OP7@% :BH7M6m3g=",ans;
    int offset=0,point=0;
    for(int i=0;i<str.size();i++){
        for(char k=32;k<=126;k++){
            if((k-32+offset)%96+32==str[i]){
                offset=k-32;
                ans+=k;
                break;
            }
        } 
    }
    for(int i=ans.size()-1;i>=0;i--){
        cout<<ans[i];
    }
}