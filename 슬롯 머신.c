#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
	int a,b,c,start;
	
	srand(time(NULL));
	
	while(1){
		printf("[Slot Machine Game]\n");
		printf("1.게임시작 // 2.나가기>>");
		scanf("%d",&start);
		if(start==1){
			a=rand()%7+33;
			b=rand()%7+33;
			c=rand()%7+33;
			printf("%c %c %c\n",a,b,c);
			if(a==b&&b==c){
				printf("jackpot!\n");
			}else{
				if(a==b || b==c || a==c){
					printf("아쉽네요.");
				}else{
					printf("운이없네요.");
				}
			}
		}else if(start==2){
			printf("안녕히가세요.");
			break;
		}else{
			printf("1.게임시작 // 2.나가기>>\n");
			printf("잘못 입력하셨습니다.");
		}
	}
}
