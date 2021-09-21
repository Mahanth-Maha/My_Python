#include <stdio.h>
#include <stdlib.h>
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
    int n, i;
    printf("Enter the no of Processes\t");
    scanf("%d", &n);
    struct process* p = (struct process *) calloc(n,sizeof(struct process));
    //struct process p[5];
    for (i = 0; i < n; i++)
    {
        p[i].pid = i;
        printf("\nEnter the burst time of process      p[%d]..", i);
        scanf("%d", &p[i].bt);
    }
    p[0].wt = awt = 0;
    p[0].tat = atat = p[0].bt;
    for (i = 1; i < n; i++)
    {
        p[i].wt = p[i - 1].wt + p[i - 1].bt;
        p[i].tat = p[i - 1].tat + p[i].bt;
        awt = awt + p[i].wt;
        atat = atat + p[i].tat;
    }
    printf("\n process\t burst time \t waiting time\ttrun around time\n");
    for (i = 0; i < n; i++)
        printf("\n p[%d]\t\t %d\t\t %d\t\t%d\t\t\n", p[i].pid, p[i].bt, p[i].wt, p[i].tat);
    printf("\n Average waiting time is:%f\nAverage tat time is:%f\n", awt / n, atat / n);
    return 0;
}