#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define XOR_KEY 0x37

unsigned char obfuscated_flag[] = { 0x43, 0x42, 0x00, 0x07, 0x43, 0x68, 0x47, 0x68, 0x7c, 0x53, 0x54, 0x44, 0x45, 0x45, 0x55, 0x45, 0x68, 0x53, 0x55, 0x5b, 0x44, 0x03, 0x45, 0x42, 0x04, 0x50, 0x59, 0x52, 0x07, 0x4c, 0x59, 0x5a, 0x45, 0x52, 0x56, 0x5e, 0x68, 0x47, 0x68, 0x03, 0x51, 0x4a, 0x68, 0x50, 0x59, 0x06, 0x03, 0x50, 0x06, 0x54 };
unsigned char shuffle_key[] = {30, 25, 14, 21, 18, 45, 32, 31, 0, 47, 24, 41, 6, 33, 48, 36, 23, 16, 4, 2, 10, 17, 26, 40, 28, 44, 29, 12, 34, 7, 9, 38, 27, 5, 1, 3, 15, 11, 20, 19, 22, 49, 39, 35, 43, 8, 37, 46, 42, 13};

void get_flag(char *output) {
    size_t flag_len = sizeof(obfuscated_flag) / sizeof(obfuscated_flag[0]);
    unsigned char temp[flag_len];

    for (size_t i = 0; i < flag_len; i++) {
        temp[shuffle_key[i]] = obfuscated_flag[i];
    }

    for (size_t i = 0; i < flag_len; i++) {
        output[i] = temp[i] ^ XOR_KEY;
    }

    output[flag_len] = '\0';
}

int main() {
    char flag[50];
    char input[10];
    int random_pin;

    srand((unsigned int)time(NULL));

    random_pin = rand() % 9000 + 1000;

    int pin_hash = (random_pin ^ 0x6969) + 0x0420;

    printf("Random PIN has been generated.\n");

    printf("Enter the 4-digit PIN: ");
    scanf("%4s", input);

    if (((atoi(input) ^ 0x6969) + 0x420) == pin_hash) {
        get_flag(flag);
        printf("Correct PIN! Here is your flag: %s\n", flag);
    } else {
        printf("Incorrect PIN. Try again.\n");
    }

    return 0;
}
