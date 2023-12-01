#include <stdio.h>
#include <stdlib.h>

// Creates a .txt file

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

    // Close the file
    fclose(fh);

    // Inform the user
    puts("File written.");

    return(0);
}
