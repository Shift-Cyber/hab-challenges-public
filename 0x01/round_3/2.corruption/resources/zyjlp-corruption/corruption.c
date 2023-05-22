#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char flag[] = "flag{baby_steps_gift_just_for_you}";

/* we provide this as a seperate function so that we actually
have a base pointer to overwrite and get returned into */
void vulnerable_function(char* input) {
    char buffer[50];
    strcpy(buffer, input);
}

void flag_function() {
    printf("%s\n", getenv("HAB_BITSANDBYTES"));
    fflush(0);
}

void controller_flag() {
    printf("%s\n", getenv("HAB_CONTROLLER"));
    fflush(0);
}

int main() {
    int stack_smash_detector = 0;
    char buffer[50];
    char input[500];
    char *secret = "UNLOCK";

    printf("You might need this: %p\n", flag_function);
    printf("this might help too: %p\n", input);

    printf("Talk to me Maverick: ");
    fflush(0);
    fgets(input, 500, stdin);
    fflush(0);

    if(strncmp(input, secret, strlen(secret)) == 0) {
        printf("Copying into the destination now...\n");
        fflush(0);

        /* ensure no overflow so we can check for smashing first */
        memcpy(buffer, input, 60);
        if(stack_smash_detector != 0) {
            printf("STACK SMASHING DETECTED... but we'll allow it ;) %s\n", getenv("HAB_COREDUMP"));
            fflush(0);
        }

        vulnerable_function(input);
    }

    return 0;
}
