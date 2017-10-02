#include<stdio.h>
#include<math.h>
long long int a[5][1000005];
int lp[100000],p[1000002];
void prime()
{
	int i,j,k=0;
	for(i=2;i<=1000;i++)
	{
		if(!p[i])
		{
		lp[k++]=i;
		for(j=i*i;j<=1000000;j+=i)
		p[j]=1;
		}
	}
	for(;i<=1000000;i++)
	if(!p[i])
	lp[k++]=i;
	lp[k++]=1000003;
}
int main()
{
	int t;
	long long int l,b;
	prime();
	scanf("%d",&t);
	// t=5;
	while(t--)
	{
		scanf("%lld%lld",&l,&b);
		// l=999999000000,b=1000000000000;
		int p,s,max,j,k=0;
		long long int sum=0,i,q;
		max=sqrt(b);
		for(i=0;i<=b-l;i++)
		a[t][i]=i+l;
		while(lp[k]<=max)
		{
			j=(lp[k]-l%lp[k])%lp[k];
			s=b-l;
			for(j;j<=s;j+=lp[k])
			{
				q=a[t][j];	
				while(q%lp[k]==0)
				{
					q=q/lp[k];
					sum+=lp[k];
				}
				a[t][j]=q;
			
			}
			k++;
		}
		for(i=0;i<=b-l;i++)
		{
			if(a[t][i]!=1)
			sum+=a[t][i];
		}
		printf("%lld\n",sum);
	}
}
