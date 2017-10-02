#include<stdio.h>
void cntgcd(long long int a,long long int b)
{
	printf("%lld %lld\n",b,a/b);
	if(a%b)
	cntgcd(b,a%b);	
}
int main()
{
	int t;
	long long int l,b;
	scanf("%d",&t);
	while(t--)
	{
	scanf("%lld%lld",&l,&b);
	if(l>b)
	{
		b=l+b;
		l=b-l;
		b=b-l;
	}
	cntgcd(b,l);	
	}
}
