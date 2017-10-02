#include<stdio.h>
#include<stdlib.h>
typedef struct nod{
	int val,c;
	struct nod *next;
}node;
int abs(int i)
{
	if(i<0)
	return -1*i;
	return i;
}
int main()
{
	int a[10001],n,qu,i,no,u,v,ab,b[10001],q[10001];
	node *nd[10001],*e[10001],*temp;
	int rear,t,end;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&qu);
		for(i=1;i<=n;i++)
		{
		a[i]=b[i]=0;nd[i]=NULL;e[i]=NULL;}
		no=0;
		for(i=1;i<=qu;i++)
		{
			scanf("%d%d%d",&u,&v,&ab);
			if(!no){
			if(u==v&&ab==1)
			no=1;
			else if(u!=v)
			{
				temp =(node*)malloc(sizeof(node));
				temp->next=NULL;
				temp->val=ab;
				temp->c=v;
				if(nd[u]==NULL)
				nd[u]=temp;
				else
				e[u]->next=temp;
				e[u]=temp;
				temp =(node*)malloc(sizeof(node));
				temp->next=NULL;
				temp->c=u;
				temp->val=ab;
				if(nd[v]==NULL)
				nd[v]=temp;
				else
				e[v]->next=temp;
				e[v]=temp;
			}
		}}
		for(i=1;i<=n;i++)
		{
		if(no==1)
		break;
		 rear=-1;
		 end=0;
		 if(!b[i]){
		q[end++]=i;
		b[i]=1;
		while(rear<end&&no==0)
		{
			
			temp=nd[q[++rear]];
			while(temp!=NULL&&no==0)
			{
				if(!b[temp->c])
				{
					b[temp->c]=1;
					a[temp->c]=abs(temp->val-a[rear]);
					q[end++]=temp->c;
				}
				else if(abs(a[temp->c]-a[q[rear]])!=temp->val)
				{
				no=1;
				//printf("%d %d ",temp->c,q[rear]);
				}
				
				temp=temp->next;				
			}
			
		}
	}}
	if(no==1)
	printf("no\n");
	else
	printf("yes\n");}
}