#include <stdio.h>
    int main()
    {
        int i,count,arr1[200],n,arr[30];
        scanf("%d", &n);
        for (i = 0; i < n;i++)
            scanf("%d", &arr[i]);
        scanf("%d",&count);
    for(i=0;i<n;i++)
    {
        arr1[(i+count)%n]=arr[i];
    }
    for(i=0;i<n;i++)
    {
        printf("%d\n",arr1[i]);
    }

    }
