#include<iostream>
#include<cstring>

using namespace std;

struct Test{
    int num;
    string ss;
    Test* next;
};


int main(int argc, char **argv){
    Test t = {1, "test", NULL};
    Test* pt = &t;
    
    int a = 20;
    
    if (pt->next != NULL){
    	cout << pt-> num << endl;
    }
    
    if (pt->next == NULL){
    	cout << "Test" << endl;
    }

    Test tt = {2,"test",NULL};
    Test* ttp = &tt;
    
    pt->next = ttp;
    if (pt-> num == 1){
    	cout << pt-> num << endl;
    	if (a > 10) {
    	    cout << 2010 << endl;
    	}
    }
    if (pt->num == 2) {
    	cout << 2 << endl;
    }
    return 0;
}
