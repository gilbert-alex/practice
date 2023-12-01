#include <stdio.h>

int main()
{
    int count=0;
    for(;;)
    {
        printf("%d, ",count);
        count++;
        if(count>50)
            break;
    }
    printf("\n");
    return(0);
}
