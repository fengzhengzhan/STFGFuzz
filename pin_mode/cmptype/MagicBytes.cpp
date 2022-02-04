#include<iostream>
#include<cstring>

using namespace std;

void bug(){
    cout << "bug" << endl;
}

int main(int argc, char **argv){
    int input;
    cin >> input;
    if(input == 15)
        bug();
    cout << input << endl;
}
