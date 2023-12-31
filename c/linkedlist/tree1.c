// implements a list of numbers as a binary search tree

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// represents a node
typedef struct node
{
    int number;
    struct node *left;
    struct node *right;
}
node;

void free_tree(node *root);
void print_tree(node *root);
bool search(node *root, int number);

int main(void)
{
    // tree of size 0
    node *tree = NULL;

    // add number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 2;
    n->left = NULL;
    n->right = NULL;
    tree = n;

    // add number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free_tree(tree);
        return 1;
    }
    n->number = 1;
    n->left = NULL;
    n->right = NULL;
    tree->left = n;

    // add number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free_tree(tree);
        return 1;
    }
    n->number = 3;
    n->left = NULL;
    n->right = NULL;
    tree->right = n;

    // print tree
    print_tree(tree);

    // ask user for target and search
    int target;
    puts("Target for search: ");
    scanf("%i", &target);

    if (search(tree, target))
    {
        printf("Target found.\n");
    }
    else
    {
        printf("Target not found.\n");
    }

    // free tree
    free_tree(tree);
    return 0;
}

// recursevely free 'left' nodes, then 'right' nodes, then root
void free_tree(node *root)
{
    if (root == NULL)
    {
        return;
    }
    free_tree(root->left);
    free_tree(root->right);
    free(root);
}

// recursevely print 'left' nodes, then root node, then 'right' nodes
void print_tree(node *root)
{
    if (root == NULL)
    {
        return;
    }
    print_tree(root->left);
    printf("%i\n", root->number);
    print_tree(root->right);
}

// 'Warning" implementation gives compile warning
// Not all control paths return a value for non-void funct
bool search(node *root, int number)
{
    if (root == NULL)
    {
        return false;
    }
    else if (number < root->number)
    {
        return search(root->left, number);
    }
    else if (number > root->number)
    {
        return search(root->right, number);
    }
    else if (number == root->number)
    {
        return true;
    }
}