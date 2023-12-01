#include <stdio.h>
#include <stdlib.h>

// reads from .txt file created in 2201.c

int main()
{
    FILE *fh;
    int ch;

    // Open the file
    fh = fopen("hello.txt","r");

    // Check for errors
    if (fh == NULL)
    {
        puts("Can't open that file.");
        return(1);
    }

    // Loop until the end-of-file
    while( !feof(fh))
    {
        // read one character
        ch = fgetc(fh);

        // end of file?
        if( ch==EOF)
            break;

        // output character
        putchar(ch);
    }

    // close the file
    fclose(fh);
    return(0);
}
