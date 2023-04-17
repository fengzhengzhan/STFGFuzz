#include <stdio.h>
#include <stdlib.h>

int check(int num) {return num;}

void crash() {
    // printf("crash");
    abort();
}

int main() {
    // Read file.
    char buf[10];
    FILE *fp = fopen("seed_file", "r");
    fgets(buf, 10, fp);

    // printf("%d", buf[0]);
    if (buf[0] >= 0x41) {
        // printf("%d", buf[0] == check(buf[0]));
        if (buf[0] == check(buf[0])) {
            // printf("%d", buf[1]);
            // printf("%d", 0x43);
            switch (buf[1]) {
                case 0x41:  return 0;
                case 0x42:  return 0;
                case 0x43:  crash();
                default: return 0;
            }
        }
    }
}

