#include <stdio.h>

void prompt();
void busy();

int main()
{
    busy();
    return(0);
}

void busy()
{
    int loop;
    char input[32];

    loop=0;
    while(loop<5)
    {
        prompt();
        fgets(input,32,stdin);
        loop++;
    }
}

void prompt()
{
    printf("C://DOS> ");
}
