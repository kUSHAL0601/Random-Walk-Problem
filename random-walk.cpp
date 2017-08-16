#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<fstream>
#include<time.h>
FILE *t;
int main()
{
	int n, N;
	n = 5000; //Ketla trials
	N = 5000; //Ketla posn possible
	t = fopen("result-1D.txt","w");
	double end[n];       
	int count[2*N+1];
	double prb[2*N+1];
	int m;
	double x, sum=0.0;
	srand(time(NULL));
	for(int i=0; i<(2*N+1); i++)      
	{
		count[i] = 0;
		prb[i] = 0.0;
	}
	for(int i=0; i<n; i++)      
	{
		end[i] = 0;
	}
	for(int i=1; i<n; i++)
	{
		m = 0;  
		for(int j=1; j<=N; j++)
		{
			x = (double)rand() / (double)RAND_MAX;
			if(x<=0.5) m++;
			if(x>0.5) m--;
		}
		end[i] = m;
	}
	for(int i=-N; i<=N; i++)
	{
		for(int j=0; j<n; j++)
		{
			if(i == end[j] ) {count[i+N]++; }
		}
	}
	for(int i=0; i<(2*N+1); i++)
	{
		prb[i] = (double)count[i]/(double)n;
		if(count[i] != 0)  fprintf(t,"%d \t %d \t %lf \n",i-N,count[i], prb[i]); 
	}
	fclose(t);
	return 0;
}
