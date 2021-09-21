#include <stdio.h>
struct process
{
    int pid;
    int bt;
    int wt;
    int tat;
};

int main()
{
    float awt, atat;
    int n, k, i, j, t, m, s[50];
    printf("Enter the no of Processes\t");
    scanf("%d", &n);
    struct process p[5];
    for (i = 0; i < n; i++)
    {
        p[i].pid = i;
        s[i] = i;
        printf("\nEnter the burst time of process p[%d]..", i);
        scanf("%d", &p[i].bt);
    }
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
            if (p[i].bt > p[j].bt)
            {
                // t=p[i].bt;
                // p[i].bt=p[j].bt;
                // p[j].bt=t;
                //t=p[i].pid;
                // p[i].pid=p[j].pid;
                // p[j].pid=t;
                t = s[i];
                s[i] = s[j];
                s[j] = t;
            }
    m = s[0];
    p[m].wt = awt = 0;
    p[m].tat = atat = p[m].bt;
    for (i = 1; i < n; i++)
    {
        m = s[i - 1];
        k = s[i];
        p[k].wt = p[m].wt + p[m].bt;
        p[k].tat = p[m].tat + p[k].bt;
        awt = awt + p[k].wt;
        atat = atat + p[k].tat;
    }
    printf("\n process\t burst time \t waiting time\ttrun around time\n");
    for (i = 0; i < n; i++)
    {
        k = s[i];
        printf("\n p[%d]\t\t %d\t\t %d\t\t%d\t\t\n", p[k].pid, p[k].bt, p[k].wt, p[k].tat);
    }
    printf("\n Average waiting time is:%f\nAverage tat time is:%f\n", awt / n, atat / n);
	return 0;
}