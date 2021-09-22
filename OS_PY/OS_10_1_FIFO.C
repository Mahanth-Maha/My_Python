#include <stdio.h>

main()
{
    int i, j, k, f, pf = 0, count = 0, pageref[25], fp[10], n;
    printf("\n Enter the length of page reference string : ");
    scanf("%d", &n);
    printf("\n Enter the reference string : ");
    for (i = 0; i < n; i++)
        scanf("%d", &pageref[i]);
    printf("\n Enter no. of frames : ");
    scanf("%d", &f);
    for (i = 0; i < f; i++)
        fp[i] = -1;
    printf("\n The Page Replacement Process is  \n");
    for (i = 0; i < n; i++)
    {
        for (k = 0; k < f; k++)
        {
            if (fp[k] == pageref[i])
                break;
        }
        if (k == f)
        {
            fp[count++] = pageref[i];
            count = (count + 1) % f;
            pf++;
            printf("\tPF No. %d", pf);
            printf("\n");
        }
        for (j = 0; j < f; j++)
            printf("\t%d", fp[j]);
        printf("\n");
    }
    printf("\n The number of Page Faults using FIFO are %d", pf);
}