#include <stdio.h>

enum {SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY};
void day_of_week(int day);

int main()
{
    int day;

    printf("Enter a weekday number, 0 - 6;\n");
    scanf("%d", &day);

    if (day < 0 || day > 6)
    {
        printf("Invalid Input\n");
        return(1);
    }
    day_of_week(day);
    return(0);
}

void day_of_week(int day)
{
        switch(day)
    {
    case SUNDAY:
        puts("Sunday");
        break;
    case MONDAY:
        puts("Monday");
        break;
    case TUESDAY:
        puts("Tuesday");
        break;
    case WEDNESDAY:
        puts("Wednesday");
        break;
    case THURSDAY:
        puts("Thursday");
        break;
    case FRIDAY:
        puts("Friday");
        break;
    case SATURDAY:
        puts("Saturday");
    }
}
