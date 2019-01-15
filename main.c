#include<stdio.h>
int main()
{
    int n,i,j,flag = 1;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n-1;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(arr[j] > arr[i])
            {
                flag = 0;
                break;
            }
        }
        if(flag == 1)
        {
            printf("%d\n",arr[i]);
        }
        flag = 1;
    }
}
