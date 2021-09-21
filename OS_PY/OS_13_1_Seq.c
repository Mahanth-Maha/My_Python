#include<stdio.h>
void main()
{
    int n,i,j,b[20],sb[20],t[20],x,c[20][20];
    printf("Enter no.of files:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
          printf("Enter no. of blocks occupied by file%d:",i+1);
          scanf("%d",&b[i]);
          printf("Enter the starting block of file%d:",i+1);
          scanf("%d",&sb[i]);
          t[i]=sb[i];
          for(j=0;j<b[i];j++)
          c[i][j]=sb[i]++;
    }
     printf("Filename\tStart block\tlength\n");
     for(i=0;i<n;i++)
      	printf("%d\t\t%d\t\t %d\n",i+1,t[i],b[i]);
}