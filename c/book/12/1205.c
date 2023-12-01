#include <stdio.h>

int main()
{
    const int n = 10;
    int highscore[n];
    int x;

    for(x=0;x<n;x++)
    {
        printf("Your #%d score: ",x+1);
        scanf("%d", &highscore[x]);
    }

    puts("Here are your high scores");
    for(x=0;x<n;x++)
    {
        printf("#%d %d\n", x+1, highscore[x]);
    }
    return(0);
}
