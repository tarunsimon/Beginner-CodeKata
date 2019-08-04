#include <stdio.h>
int main()
{
    int n,a=1,k=0,i;
    scanf("%d%d", &n,&k);
    for(i=1;i<=k;i++)
    {
      a=a*n;
    }
    printf("%d",a);
}
