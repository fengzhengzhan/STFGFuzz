#include <stdio.h>

void a(int x){
    printf("funca%d", x);
}

void b(int x){
    printf("funcb%d", x);
}

void c(int x){
    printf("funcc%d", x);
}

int main() {
    int x = 10;
    if (x > 5) {
        a(x);
    } else {
        b(x);
    }
    c(x);
    return 0;
}