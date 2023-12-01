#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


int main()
{
    float *temp;
    char temp_type;

    temp = (float *)malloc(sizeof(float) *1);
    if(temp == NULL)
    {
        puts("Unable to allocate memory");
        return(1);
    }

    printf("What is the temperature? ");
    scanf("%f", temp);
    getchar();
    printf("Fahrenheit or Celsius? (F/C) ");
    temp_type = getchar();

    if (toupper(temp_type) == 'C')
    {
        *temp += 273.15;
    }
    else if (toupper(temp_type) == 'F')
    {
        *temp = (*temp + 459.67) * (5.0/9.0);
    }
    else
    {
        printf("Invalid use");
        return(1);
    }


    printf("The temperature in Kelvin is %.2f\n", *temp);
    return(0);

}
