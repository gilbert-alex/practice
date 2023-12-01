#include <stdio.h>
#include <stdlib.h>

// Saves 5 scores as binary data to a file scores.dat

int max = 5;

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

    int x = 0;
    while(x < max)
    {
        printf("High Score %d/%d: ", x+1, max);
        scanf("%d",&highscore);
        fwrite(&highscore,sizeof(int),1,handle);
        puts("Score saved");
        x++;
    }
    fclose(handle);
    return(0);
}
