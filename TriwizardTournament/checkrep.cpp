#include<stdio.h>
typedef struct nodes{
	long long int val;
	int ind;
}node;
int s[100001],e[100001];
node a[100001],b1[100001];
long long int x;
void merging(int low,int mid,int high) {
   int l1, l2, i;
 
   for(l1 = low, l2 = mid + 1, i = low; l1 <= mid && l2 <= high; i++) {
      if(a[l1].val < a[l2].val)
         b1[i] = a[l1++];
     else if(a[l1].val==a[l2].val)
	  {
	  	if(a[l1].ind<a[l2].ind)
	  	b1[i]=a[l1++];
	  	else
	  	b1[i]=a[l2++];
		}   
      else
         b1[i] = a[l2++];
   }
   while(l1 <= mid)    
      b1[i++] = a[l1++];
 
   while(l2 <= high)   
      b1[i++] = a[l2++];
 
   for(i = low; i <= high; i++)
      a[i] = b1[i];
}
void sort(int low,int high) {
  int mid;
    if(low < high) {
      mid = (low + high) / 2;
      sort(low, mid);
      sort(mid+1, high);
      merging(low, mid, high);
   }else { 
      return;
   }   
}
int binaryval(int low,int high) 
{
	int mid=(low+high)/2;
	if(a[mid].val==x)
	return mid;
	if(low==high)
	return -1;
	if(a[mid].val<x)
	return binaryval(mid+1,high);
	return binaryval(low,mid-1);
}
int binaryind(int low,int high,int l) 
{
	int mid=(low+high)/2;
	if(a[low].ind>l)
	return low;
	if(a[high].ind<l)
	return high;
	if(a[mid].ind==l)
	return mid;
	if(a[mid].ind<l)
	return binaryind(mid+1,high,l);
	return binaryind(low,mid-1,l);
}
int main()
{
	int n,t,i,j,l,r,l1,r1,p,q,y,in,qu;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&qu);
		for(i=0;i<n;i++)
		{
			scanf("%lld",&(a[i].val));
			a[i].ind=i;
		}
		sort(0,n-1);
		for(i=0;i<n;i++)
		{
			s[i]=i;
			j=i;
			while(a[i].val==a[i+1].val&&i+1<n)
				s[++i]=j;
			for(;j<=i;j++)
			e[j]=i;	
		}				
		while(qu--)
		{
		scanf("%d%d%lld%d",&l,&r,&x,&y);
		in=binaryval(0,n-1);
		if(in==-1)
		printf("NO\n");
		else
		{
		 	p=s[in];
		 	q=e[in];
		 	l1=binaryind(p,q,l);
		 	r1=binaryind(p,q,r);
		 	if(a[r1].ind<l)
		 	printf("NO\n");
		 	else if(r1-l1+1>=y)
		 	printf("YES\n");
		 	else
		 	printf("NO\n");
		} 	
		}			
	}
}
