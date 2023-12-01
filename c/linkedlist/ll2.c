// prepends numbers to a linked list, using for loop to print
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(int argc, char *argv[])
{
    // memory for numbers
    node *list = NULL;

        // for each command-line argument
        for (int i = 1; i < argc; i++)
        {
            // convert argument to int
            int number = atoi(argv[i]);

            // allocate node for number
            node *n = malloc(sizeof(node));
            if (n == NULL)
            {
                return 1;
            }
            n->number = number;
            n->next = NULL;

            // prepend node to list
            n->next = list;
            list = n;
        }

    // print numbers
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
    {
        printf("%i\n", ptr->number);
    }

    // free memory
    node *ptr = list;
    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }
}