#include <stdio.h>
int main()
{
    int r,n,i,c=0;
    scanf("%d %d",&r,&n);
    for(i=0;i<=n;i++)
    {
    if(pow(2,i)==r)
    ++c;
    }
    if(c>0)
    printf("yes");
    else
    printf("no");
    return 0;
}
