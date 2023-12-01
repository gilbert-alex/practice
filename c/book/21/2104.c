#include <stdio.h>
#include <time.h>

int main()
{
    time_t tictoc = 946684800;
    printf("%s\n", ctime(&tictoc));
    return(0);
}
