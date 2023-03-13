#include <stdio.h>
#include <string.h>

int main()
{
    /* flag{bob_the_architect} ^ \x2E */
    char * ct = "\x48\x42\x4f\x49\x55\x4c\x41\x4c\x71\x5a\x46\x4b"
                "\x71\x4f\x5c\x4d\x46\x47\x5a\x4b\x4d\x5a\x53";

    /* decrypt and write to stdout */
    for (int i=0; i < strlen(ct); i++) { printf("%c", ct[i] ^ 46); }
    puts("\n");
}