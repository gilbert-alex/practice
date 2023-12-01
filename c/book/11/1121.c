#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int random = srand((unsigned)time(NULL));
    int secret = random % 10;
    int guess;

    printf("Can you guess the secret number: ");
    scanf("%d", &guess);
    if(guess==secret)
    {
        puts("You guessed it!");
        return(0);
    }
    if(guess!=secret)
    {
        printf("The secret number was %d.",secret);
        return(1);
    }
}
