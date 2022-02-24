#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <getopt.h>
#include <stdlib.h>

#define N 201
#define BUFFERN 44

using namespace std;

int main(int argc, char *argv[]) {

    int opt, opt_index;
    char* filename;
    static struct option long_options[] = 
    {
        {"file", required_argument, NULL, 'f'}
    };
    while((opt = getopt_long(argc, argv, "f:", long_options, &opt_index)) != -1)
    {
        switch (opt)
        {
        case 'f':
            filename = optarg;
            break;
        
        default:
            printf("Error Parameters!");
            break;
        }

    }

    // Read file.
    char str[N];
    FILE *fp = fopen(filename, "r");
    fgets(str, N, fp);
    // printf("%s", str);
    
    // printf("%ld", sizeof(char)*BUFFERN);
    char buffer[45] = {};
    memcpy(buffer, str, sizeof(char)*BUFFERN);
    printf("---------------------   %c", buffer[44]);
    buffer[44] = '\0';
    // buffer   
    // printf("%s\n", buffer);


    if (memcmp(&buffer[0], "The quick brown fox ", 20) != 0 ||
        strncmp(&buffer[20], "jumps over ", 11) != 0 ||
        strcmp(&buffer[31], "the lazy dog.") != 0) {
    return 1;
    }

    printf("Though first str/mem Cmp.\n");

    char s1[N], s2[N], s3[N];
    for (int i = 0; i < 16; i ++) {
        s1[i] = str[i+BUFFERN];
    }
    s1[16]='\0';
    for (int i = 0; i < 8; i ++) {
        s2[i] = str[i+BUFFERN+16];
    }
    s2[8]='\0';
    for (int i = 0; i < 4; i ++) {
        s3[i] = str[i+BUFFERN+16+8];
    }
    s3[4]='\0';
    printf("%s\n", s3);

    uint64_t x = strtoull(s1, NULL, 16);
    if (x != 0xCAFEBABECAFEBABE) {
        return 1;
    }

    uint32_t y = strtoul(s2, NULL, 16);
    if (y != 0xDEADC0DE) {
        return 1;
    }

    uint16_t z = strtouq(s3, NULL, 16);
    // printf("%d %d\n", z, 0xBEEF);
    switch (z) {
    case 0xBEEF:
        break;

    default:
        return 1;
    }

    printf("Puzzle solved, Congratulations!\n");
    return 0;
}