#include <stdio.h>

int main()
{
    int highscore[4];

    for(int x = 0; x < 4; x++)
    {
        printf("Your #%d score: ", x+1);
        scanf("%d", &highscore[x]);
    }

    puts("Here are your high scores");
    for(int y = 0; y < 4; y++)
    {
        printf("#%d %d\n", y, highscore[y]);
    }
    return(0);
}
