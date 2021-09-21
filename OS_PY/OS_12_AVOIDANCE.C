
#include <stdio.h>

struct da{
    int max[10], al[10], need[10], before[10], after[10];
} p[10];

int main()
{
    int i, j, k, l, r, n, tot[10], av[10], cn = 0, cz = 0, temp = 0, c = 0;
    printf("\n ENTER THE NO. OF PROCESSES:");
    scanf("%d", &n);
    printf("\n ENTER THE NO. OF RESOURCES:");
    scanf("%d", &r);
    for (i = 0; i < n; i++){
        printf("PROCESS %d \n", i + 1);
        for (j = 0; j < r; j++){
            printf("MAXIMUM VALUE FOR RESOURCE %d:", j + 1);
            scanf("%d", &p[i].max[j]);
        }
        for (j = 0; j < r; j++){
            printf("ALLOCATED FROM RESOURCE %d:", j + 1);
            scanf("%d", &p[i].al[j]);
            p[i].need[j] = p[i].max[j] - p[i].al[j];
        }
    }
    for (i = 0; i < r; i++)
    {
        printf("ENTER TOTAL VALUE OF RESOURCE %d:", i + 1);
        scanf("%d", &tot[i]);
    }
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < n; j++)
            temp = temp + p[j].al[i];
        av[i] = tot[i] - temp;
        temp = 0;
    }
    printf("\n\t RESOURCES  ALLOCATED   NEEDED   TOTAL  AVAIL");
    for (i = 0; i < n; i++)
    {
        printf("\n P%d \t", i + 1);
        for (j = 0; j < r; j++)
            printf("%d", p[i].max[j]);
        printf("\t");
        for (j = 0; j < r; j++)
            printf("%d", p[i].al[j]);
        printf("\t");
        for (j = 0; j < r; j++)
            printf("%d", p[i].need[j]);
        printf("\t");
        for (j = 0; j < r; j++)
        {
            if (i == 0)
                printf("%d", tot[j]);
        }
        printf("    ");
        for (j = 0; j < r; j++)
        {
            if (i == 0)
                printf("%d", av[j]);
        }
    }
    printf("\n\n\t AVAIL  BEFORE \t   AVAIL AFTER ");
    for (l = 0; l < n; l++)
    {
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < r; j++)
            {
                if (p[i].need[j] > av[j])
                    cn++;
                if (p[i].max[j] == 0) //check if a process requires no resources
                    cz++;
            }
            if (cn == 0 && cz != r) //if needed resources are available
            {
                for (j = 0; j < r; j++)
                {
                    p[i].before[j] = av[j] - p[i].need[j];
                    p[i].after[j] = p[i].before[j] + p[i].max[j];
                    av[j] = p[i].after[j];
                    p[i].max[j] = 0;
                }
                printf("\n P %d \t", i + 1);
                for (j = 0; j < r; j++)
                    printf("%d", p[i].before[j]);
                printf("\t");
                for (j = 0; j < r; j++)
                    printf("%d", p[i].after[j]);
                cn = 0;
                cz = 0;
                c++; //safesequence count
                break;
            }
            else
            {
                cn = 0;
                cz = 0;
            }
        }
    }
    if (c == n)
        printf("\n THE ABOVE SEQUENCE IS A SAFE SEQUENCE");
    else
        printf("\n DEADLOCK OCCURED");
	return 0;
}