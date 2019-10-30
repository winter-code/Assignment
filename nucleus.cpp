#include<bits/stdc++.h>
#include<iostream> 
using namespace std;

int main()
{
	int n;
	cin>>n;
	int arr[n][n];
	for(int i=0; i<n;i++){
		for(int j=0; j<n;j++){
		cin>> arr[i][j];
	}
	}

	for(int i=0; i<n;i++){
		for(int j=0; j<n;j++){
		cout<< arr[i][j]<<" ";
	}
	}

	int s[7] = {};
	
	int sum=0, j=0;

	for(int i=0, j=0;i<n;i++){
		if(i==0 && j==0){ sum+=arr[i][j]; s[i]=sum; continue;}
		int m=i;
		
			while(j<n && m>=0){
			sum += arr[m][j];
			m=m-1;
			j=j+1;
		}
		s[i] = sum;
		sum=0;

	}

	int i=n;
	for(int j=0; j<n; j++)
	{
		int m=i;
		int l=m+j;
		
			while(j<n && m>=0){
			sum += arr[m][j];
			m=m-1;
			j=j+1;
		}
		s[l] = sum;
		sum=0;
		
	}

	for(int k=0; k< 7; k++){
		cout<<" Output : " << s[k] << " ";
	}
	
}
