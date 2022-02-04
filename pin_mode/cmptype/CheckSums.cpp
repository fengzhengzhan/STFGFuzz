#include<iostream>
#include<cstring>

using namespace std;

void bug(){
    cout << "bug" << endl;
}

int main(int argc, char **argv){
    int input;
    cin >> input;
    int l;
    l = sizeof(input);
    if(input+10 == input*2+l)
        bug();
    cout << input << ":" << l << endl;
}
