#include <bits/stdc++.h>
using namespace std;
 
#define PB push_back
#define F first
#define S second
#define MP make_pair
#define LL long long
#define MOD1 1000000007
#define MOD2 1000000009
#define pr(i,x,n) for(int ii=i;ii<n+i;ii++){cout<<x[ii]<<" ";}cout<<endl;
#define ip(i,x,n) for(int ii=i;ii<n+i;ii++){cin>>x[ii];};
#define db(x,y) cout<<x<<" "<<y<<endl;
#define N 10000002
 
int main()
{
    long long r,op[N],i,j,c,k,d,x,t,a[10000001],tc[10000001],y,l,m,n;
    unsigned long long ans;
    cin>>t;
    op[1]=0;
    for(i=2;i<N;i++)
    op[i]=1;
    for(i=2;i<N;i++)
    {
        if(op[i]==1)
        {
            for(j=i+i;j<N;j+=i)
            op[j]=0;
        }
    }
    
    while(t--)
    {
        cin>>l>>r;
        for(i=0;i<=r-l;i++)
        {
        a[i]=0;
        tc[i]=i+l;
        }
        //cout<<"ss";
        for(i=2;i<N;i++)
        {
            if(op[i]==1)
            {
                m=floor(l/i);
                j=m*i;
                while(j<l)
                j+=i;
                for(;j<=r;j+=i)
                {
                k=j;
                while(k%i==0)
                {
                a[j-l]+=i;
                k/=i;
                }
                while(tc[j-l]%i==0)
                tc[j-l]/=i;
                }
            }
        }
        ans=0;
        for(i=0;i<=r-l;i++)
        {
            //db(i+l,a[i]);
        ans+=a[i];
        if(tc[i]>=N)
        ans+=tc[i];
        }
        cout<<ans<<endl;
    }
    return 0;
} 