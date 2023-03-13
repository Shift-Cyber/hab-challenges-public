#include <stdio.h>
#include <string.h>

int main()
{
    /* flag{its_just_an_address_man} ^ \x2E */
    char * ct = "\x48\x42\x4f\x49\x55\x47\x5a\x5d\x71\x44\x5b\x5d\x5a\x71"
                "\x4f\x40\x71\x4f\x4a\x4a\x5c\x4b\x5d\x5d\x71\x43\x4f\x40\x53";

    /* decrypt and write to stdout */
    for (int i=0; i < strlen(ct); i++) { printf("%c", ct[i] ^ 46); }
    puts("\n");
}
