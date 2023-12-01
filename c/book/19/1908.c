#include <stdio.h>

int main()
{
    char alphabet[26];
    char *pa;               // empty pointer

    pa = alphabet;          // initialize to alphabet

    for (int x = 0; x < 'Z'; x++)    // fill array with letters starting at A and incrementing by one for each arr pos
    {
        *pa++ = x + 65;
    }

    pa = alphabet;          // re-initialize to beginning of alphabet array

    for (int x=0; x < 26; x++)      // print each position of the alpha arr by reference via pointer notation
    {
        printf("%c, ", *pa);
        pa++;
    }
    return(0);
}
