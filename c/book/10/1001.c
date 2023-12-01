#include <stdio.h>

// prototype
void prompt();

int main()
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
    return(0);
}

void prompt()
{
    printf("C://DOS> ");
}
