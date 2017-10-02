#include<stdio.h>
long long int xs[262145]={0};
int s[262145],i,j,k;
int a[100005],n,qu,i,no,u,v,ab,b[100001],q[100005];
node *nd[200005],*e[200005],*temp;
void sd(int xl,int xh,int yl,int yh)
{
    if(xh-xl<=1)
	if(xl!=xh){
	int i,j=1,l,b;
	l=(xl+xh)/2;b=(yl+yh)/2;
	for(i=yl+1;i<b;i++)
	{st[i]^=b[l-j]^b[l];j++;
	};
	sd(xl,l,yl,b);
	sd(xl,l,b+1,yh);
	sd(l+1,xh,yl,b)
	}
	
}
int main()
{

	scanf("%d%lld",&n,&d);
	for(i=0;i<n-1;i++)
	{
		scanf("%d%d",&u,&v);
		temp =(node*)malloc(sizeof(node));
		temp->next=NULL;
		temp->c=v;
		if(nd[u]==NULL)
		nd[u]=temp;
		else
		e[u]->next=temp;
		e[u]=temp;
		temp =(node*)malloc(sizeof(node));
		temp->next=NULL;
		temp->c=u;
		if(nd[v]==NULL)
		nd[v]=temp;
		else
		e[v]->next=temp;
		e[v]=temp;	
	}
	xs[0]=val[0];
	s[p]=0;
	while(p>=0)
	{
		if(!q[s[p]])
		{
			q[s[p]]=1;
			if(nd[s[p]]!=NULL)
			while(q[nd[s[p]]->c])
			{
				nd[s[p]]=nd[s[p]]->next;
				if(nd[s[p]]==NULL)
				break;
			}
			if(nd[s[p]]!=NULL){
			s[++p]=nd[s[p-1]]->c;
			xs[p]^=a[s[p]];
			if(max<p)
			max=p;
			}
        }
        else if(nd[s[p]]!=NULL){
            if(nd[s[p]]!=NULL)
			while(q[nd[s[p]]->c])
			{
				nd[s[p]]=nd[s[p]]->next;
				if(nd[s[p]]==NULL)
				break;
			}
			if(nd[s[p]]!=NULL){
			s[++p]=nd[s[p-1]]->c;
			xs[p]^=a[s[p]];
			if(max<p)
			max=p;
			}
        }
    }
    for(i=0;i<20;i++)
    if(p>pw)
    pw*=2;
    b[pw]=val[0];
    st[pw]=val[0];
    for(i=pw-1;i>=0;i++)
    {
        b[i]^=b[i+1]^val[j++];
        st[i]=b[i];
    }

}