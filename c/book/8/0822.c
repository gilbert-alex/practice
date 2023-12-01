#include <stdio.h>

int a,b;

int main()
{
    printf("Enter value A: ");
    scanf("%d",&a);
    printf("Enter value B: ");
    scanf("%d",&b);

    if(a>b)
        printf("%d is larger than %d.\n",a,b);
    else if(a<b)
        printf("%d is larger than %d.\n",b,a);
    else
        printf("%d and %d are the same.\n",a,b);

    return(0);
}
