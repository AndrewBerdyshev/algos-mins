#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void lsd_radix_sort(size_t ALen, size_t strLen, char A[ALen][strLen], size_t index)
{
    size_t CLen = 1<<8-1;
    char C[1<<8];
    memset(C, 0, CLen);
    for(size_t i = 0; i < ALen; i++) C[A[i][0]] += 1;
}

static char strings[][5] = {
    "pzazz",
    "jazzy",
    "qujaq",
    "fezzy",
    "fizzy",
    "fuzzy",
    "whizz",
    "buzzy",
    "muzzy",
    "phizz"
};

int main()
{
    lsd_radix_sort(10, 5, strings, 0);
    return 0;
}