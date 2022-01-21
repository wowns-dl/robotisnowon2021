#include <stdio.h>
int main(){
	int x=0,y=0,z=0,n=0;
	printf("물건값:");
	scanf("%d",&x);
	printf("낸값:");
	scanf("%d",&y);
	if(y-x<0){
		printf("돈더내세요");
	}
	else{
		printf("거스럼돈:");
		printf("%d",y-x);
		if(y-x>=10000){
			z=(y-x)/10000;
			n=(y-x)%10000;
			printf("\n만원권:%d",z);
		}
		else{
			if(n->=5000){
				z=(y-x)/5000;
				n=(y-x)%5000;
				printf("\n오천원권:%d",z);
			}
		}
	}
}
