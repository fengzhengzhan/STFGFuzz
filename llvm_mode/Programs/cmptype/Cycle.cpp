#include<iostream>
#include<cstring>

using namespace std;

void bug(){
    cout << "bug" << endl;
}

int main(int argc, char **argv){
    string input;
    cin >> input;
    string temp;
    for (int i = 0; i < input.length()+1; i++)
    {
        if (input[i] != '\0')
        {
            cout << input[i] << endl;
        }
        else
        {
            bug();
        }
    }
    
    cout << input << ":" << input.length() << endl;
}
