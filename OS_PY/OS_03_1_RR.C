#include <stdio.h>
#include <math.h>

struct process
{
    int pid;
    int bt;
    int wt;
    int tat;
    int et;
};

int main()
{
    float awt, atat;
    int n, i, j, qt, max = 0;
    printf("Enter the no of Processes\t");
    scanf("%d", &n);
    struct process p[5];
    printf("enter quantum time");
    scanf("%d", &qt);
    for (i = 0; i < n; i++)
    {
        p[i].pid = i;
        printf("\nEnter the burst time of process p[%d]..", i);
        scanf("%d", &p[i].bt);
        p[i].et = p[i].bt;
        if (max < p[i].bt)
            max = p[i].bt;
    }
    awt = 0;
    atat = 0;
    p[-1].wt = p[-1].bt = 0;
    for (j = 0; j < ceil(max / qt); j++)
    {
        for (i = 0; i < n; i++)
        {
            if (p[i].bt != 0)
            {
                if (p[i].bt < qt)
                {
                    p[i].wt = p[i - 1].wt + p[i - 1].bt;
                    p[i].tat = p[i].wt + p[i].bt;
                    p[i].bt = 0;
                }
                else
                {
                    p[i].wt = p[i - 1].wt + qt;
                    p[i].tat = p[i - 1].tat + qt;
                    p[i].bt -= qt;
                }
                awt = awt + p[i].wt;
                atat = atat + p[i].tat;
                printf(" process %d", p[i].pid);
            }
        }
        printf("\n process\t burst time \t waiting time\ttrun around time\n");
        for (i = 0; i < n; i++)
            printf("\n p[%d]\t\t %d\t\t %d\t\t%d\t\t\n", p[i].pid, p[i].bt, p[i].wt, p[i].tat);
        printf("\n Average waiting time is:%f\nAverage tat time is:%f\n", awt / n, atat / n);
        return 0;
    }
}