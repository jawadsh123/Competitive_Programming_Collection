#include<stdio.h>
#include<string.h>
int main()
{
	char a[100005],x;
	int c=0,n,i,t;
	// FILE *fp  = fopen("test.txt", "r");
	// FILE *ofp  = fopen("output.txt", "w");
	scanf("%d",&t);
	// scanf("%c",&x);
	
	while(t--){
	c=0;	
	scanf("%s",a);
	n=strlen(a);
	for(i=n-1;i>=0;i--)
	c=c+(c+a[i]-'0')%2;
	printf("%d\n",c);}
} 
