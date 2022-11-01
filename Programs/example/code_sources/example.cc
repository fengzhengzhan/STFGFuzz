#include <cstdio>

using namespace std;

void crash(){
}

int main(int argc, char *argv[]) {

    int x = 0;
//    scanf("%d", &x);

    if (x == 0xBEEF) {
        printf("magic");
    }

    if (x/100 == x%100+17) {
        crash();
    } else {
        printf("checksum");
    }

    int i = 0;
    for(i = 0; i < 100; ++ i) {
        x ++ ;
    }
//    int i = 2;
//    while(i > 5) {
//        i--;
//    }

    return 0;
}
