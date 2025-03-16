#include <stdio.h>
#include <stdlib.h>

int i = 0, t = 1;
char str[20];

void E();
void EPRIME();
void T();
void TPRIME();
void F();
void error();

int main() {
    printf("The given grammar is:\n");
    printf("\nE -> TE'");
    printf("\nE' -> +TE'/$");
    printf("\nT -> FT'");
    printf("\nT' -> *FT'/$");
    printf("\nF -> (E)/a");
    
    printf("\nEnter the string to be parsed: ");
    scanf("%s", str);
    
    E();
    
    if (t != 1 || str[i] != '\0') {
        printf("\nGiven string is not accepted\n");
    } else {
        printf("\nThe given string is accepted\n");
    }

    return 0;
}

void E() {
    T();
    EPRIME();
}

void EPRIME() {
    if (str[i] == '+') {
        i++;
        T();
        EPRIME();
    }
}

void T() {
    F();
    TPRIME();
}

void TPRIME() {
    if (str[i] == '*') {
        i++;
        F();
        TPRIME();
    }
}

void F() {
    if (str[i] == 'a') {
        i++;
    } else if (str[i] == '(') {
        i++;
        E();
        if (str[i] == ')') {
            i++;
        }
    } else {
        error();
    }
}

void error() {
    t = -1;
}


OUTPUT

The given grammar is:

E -> TE'
E' -> +TE'/$
T -> FT'
T' -> *FT'/$
F -> (E)/a
Enter the string to be parsed: a+a*a

The given string is accepted
