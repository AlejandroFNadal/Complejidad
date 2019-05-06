#include <stdio.h>
int mcd(int a, int b);
int mcm(int a, int b);

int main()
{
printf("%d",mcm(72,50));
}

int mcd(int a, int b)
{
    int k=1;
    if(a==0) return b;
    if(b==0) return a;
    if(a != 0 && b != 0)
    {
        k=k* mcd(b,a % b);
        return k;
    }
}
int mcm(int a, int b)
{
    return (a*b)/mcd(a,b);
}
