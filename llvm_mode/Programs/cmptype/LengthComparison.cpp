#include<iostream>
#include<cstring>

using namespace std;

void bug(){
    cout << "bug" << endl;
}

int main(int argc, char **argv){
    string input;
    cin >> input;
    if(input.length() > 8)
        bug();
    cout << input << ":" << input.length() << endl;
}
