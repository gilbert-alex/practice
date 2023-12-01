#include <stdio.h>

int main()
{
    struct score
    {
        char name[32];
        int score;
    };
    struct score player[4];

    int x;

    for (x = 0; x < 4; x++)
    {
        printf("Enter player %d: ", x+1);
        scanf("%s", player[x].name);
        printf("Enter their score: ");
        scanf("%d", &player[x].score);
    }

    puts("Player Info");
    printf("#\tName\tScore\n");

    for (x = 0; x < 4; x++)
    {
        printf("%d\t%s\t%5d\n", x+1, player[x].name, player[x].score);
    }
    return(0);
}
