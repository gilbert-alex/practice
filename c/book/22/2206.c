#include <stdio.h>
#include <stdlib.h>

// Writes a single score as plain text to a file scores.dat via printf

int main()
{
    FILE *handle;
    int highscore;

    handle = fopen("scores.dat","w");
    if(!handle)
    {
        puts("File error.");
        exit(1);
    }
    printf("What is your high score? ");
    scanf("%d",&highscore);
    fprintf(handle,"%d",highscore);
    fclose(handle);
    puts("Score saved");
    return(0);
}
