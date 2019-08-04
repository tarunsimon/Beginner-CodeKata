#include <stdio.h>
int main()
{
    int n,k,l,a[10],i,d=0;
    scanf("%d%d", &n,&k);
    for(i=0;i<n;i++)
    {
    scanf("%d",&a[i]);
    }
    for(i=0;i<k;i++)
    {
      d = d + a[i];

    }
    printf("%d",d);
}
