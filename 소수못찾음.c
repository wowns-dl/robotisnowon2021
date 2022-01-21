#include <stdio.h>
int main(){
	int num,i,stop=0;
	scanf("%d",num);
	for(i=2;i<num;i++){
		if(num%i==0){
			stop++;
		}
	}
		if(stop==0){
			printf("소수");
		}else{
			printf("소수아님");
		}
	return 0;
}
