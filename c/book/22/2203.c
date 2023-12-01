#include <stdio.h>
#include <stdlib.h>

// Creates a .txt file with an additional line of text over 2201.c

int main()
{
    FILE *fh;

    // Open the file
    fh = fopen("hello.txt","w");

    // Check for errors
    if (fh == NULL)
    {
        puts("Can't open that file!");
        return(1);
    }

    // Output text
    fprintf(fh, "Look what I made!\n");
    fputs("My C program wrote this file.\n", fh);

    // Close the file
    fclose(fh);

    // Inform the user
    puts("File written.");

    return(0);
}
