#include <stdio.h>
void printf(int a[5][5]){
	for (int i=0;i<5;i++){	
		for(int j=0; j<5; j++){
			printf("%3d",a[i][j]);
		}
		printf("\n");
	}
}

int main(){
	int a[5][5]={0,};
	int c=1;
	for(int i=0;i<5;i++){
		for(int j=0;j<5;j++){
			a[i][j]=c++;
		}
	}
	printf(a);
}
