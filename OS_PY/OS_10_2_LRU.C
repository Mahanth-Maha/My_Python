#include <stdio.h>
main()
{
    int i, j, k, f, max, p = 10, pf = 0, count[10], pageref[25], fp[10], n, flag[10];
    printf("\n Enter the length of page reference string :");
    scanf("%d", &n);
    printf("\n Enter the reference string :");
    for (i = 0; i < n; i++)
        scanf("%d", &pageref[i]);
    printf("\n Enter no. of frames :");
    scanf("%d", &f);
    for (i = 0; i < f; i++)
    {
        fp[i] = -1;
        count[i] = 0;
        //flag[i] = 0;
    }
    printf("\n The Page Replacement Process is -- \n");
    for (i = 0; i < n; i++)
    {
        for (k = 0; k < f; k++)
        {
            if (count[k] == 0)
            {
                fp[k] = pageref[i];
                pf++;
                count[k] = 1;
                p = k;
                //flag[k] = 1;
                break;
            }
            else if (fp[k] == pageref[i]) //required page found
            {
                count[k] = 1;
                p = k;
                //flag[k] = 1;
                break;
            }
        }
        if (k == f) //LRU replacement
        {
            max = 0;
            for (j = 0; j < f; j++)
            {
                if (count[j] > max)
                {
                    max = count[j];
                    p = j;
                }
            }
            fp[p] = pageref[i];
            count[p] = 1;
            //flag[p] = 1;
            pf++;
        }
        printf("Page ref is %d Fault %d", pageref[i], pf);
        for (j = 0; j < f; j++)
        {
            if (j == p || count[j] == 0)
                continue;
            count[j] = count[j] + 1;
            //printf("\t%d %d",fp[j],count[j]);
            //if((count[j]!=0)&&(flag[j]!=1))
            //count[j]+=1;
            //printf("count is %d",count[j]);
        }
        for (j = 0; j < f; j++)
        {
            printf("\t%d %d", fp[j], count[j]);
        }
        printf("\n");
    }
    printf("\n The number of Page Faults using LRU are %d", pf);
}