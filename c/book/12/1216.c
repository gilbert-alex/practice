#include <stdio.h>

int main()
{
    const int length = 21;
    char phrase[] = "C programming is fun!";
    int inner, outer, temp, x;

    printf("%s\n", phrase);

    for(outer = 0; outer < length - 1; outer++)
    {
        for(inner = outer +1; inner < length; inner++)
        {
            if(phrase[outer] > phrase[inner])
            {
                temp = phrase[outer];
                phrase[outer] = phrase[inner];
                phrase[inner] = temp;
            }
        }
    }

    printf("%s\n", phrase);
    return(0);
}
