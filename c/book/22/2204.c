#include <stdio.h>
#include <stdlib.h>

// reads text from hello.txt 64 chars at a time (including new line)

int main()
{
    FILE *fh;
    char buffer[64];
    char *r;

    fh = fopen("hello.txt","r");
    if( fh == NULL)
    {
        puts("Can't open that file.");
        exit(1);
    }

    while( !feof(fh))
    {
        // fgets return (char *)NULL on error or EOF
        // fgets return address of buffer to r which is a char pointer
        r = fgets(buffer,64,fh);
        if( r==NULL)
            break;
        printf("%s",buffer);
    }
    fclose(fh);
    return(0);
}
