#include <stdio.h>
#include <string.h>

int main() {
    char input[50];
    char password[] = "RE_using_ghidra";

    printf("Welcome to the password cracking challenge!\n");
    printf("Enter the password to get the flag: ");
    scanf("%49s", input);

    if (strcmp(input, password) == 0) {
        printf("Flag: Kaliber{Pl41n73x7_1s_b4d_3v3n_c0mp1l3d}\n");
    } else {
        printf("Incorrect password. Try again!\n");
    }

    return 0;
}
