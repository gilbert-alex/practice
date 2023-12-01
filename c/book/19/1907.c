#include <stdio.h>

int main()
{
    char alphabet[26];
    char *pn;

    pn = alphabet;

    for (int x = 0; x<26; x++)
    {
        *pn = x + 'A';
        pn++;
    }

    pn = alphabet;

    for (int x = 0; x < 26; x++)
    {
        printf("%c, ", *pn);
        pn++;
    }
    return(0);
}
