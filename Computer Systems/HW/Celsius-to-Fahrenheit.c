/*
*   Author: John Marangola - marangol@bc.edu
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

double convert(double celsius);
int all_digits(char *input);

int main(int argc, char *argv[]) {
    char *eptr;
    if (argc > 1) {
        if (all_digits(argv[1]) == 0) {
            printf("Error, must enter an integral value for temperature.\n");
            return -1;
        }
        printf("Celsius: %.2f | Fahrenheit: %.2f\n", strtod(argv[1], NULL), convert(strtod(argv[1], NULL)));
        return 0;  
    }
    else {
        printf("Error. Missing have CLi temperature argument.\n");
        return -1;
    }
}

double convert(double celsius) {
    return ((celsius * 9.0)/5.0  + 32);
}

int all_digits (char *input) {
    char str[1000];
    strcpy(str, input);
    for (int i = 0; i < strlen(input); i++) {
        if (!isdigit(str[i]) && str[i] != '.' && (str[i] == '-' && i != 0))
            return 0; 
    }
    return 1;
}