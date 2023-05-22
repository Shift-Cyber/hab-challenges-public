#include <stdio.h>

int main(int argc, char *argv[]) {
    FILE *file;
    char ch;

    // Check if a filename argument is provided
    if (argc < 2) { return 1; }

    // Open the file in read mode
    file = fopen(argv[1], "r");
  
    // Check if the file was opened successfully
    if (file == NULL) {
        printf("An error occured.\n");
        return 1;
    }

    // Read and print each character from the file
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    // Close the file
    fclose(file);

    return 0;
}