#include <stdio.h>
int main()
{
    long long num;
    int count = 0;
    scanf("%lld", &num);
    while(num != 0)
    {
       
        num /= 10;
        ++count;
    }
    printf("Number of digits: %d", count);
}
