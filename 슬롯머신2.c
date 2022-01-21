include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
	int a,b,c,start;

	srand(time(NULL));

	while(1){
		printf("[Slot Machine Game]\n");
		printf("숫자를입력후 'Enter'키를 누르세요.\n");
		printf("1.게임시작 // 2.나가기 // 3.게임설명>>");
		scanf("%d",&start);
		if(start==1){
			a=rand()%6+33;
			b=rand()%6+33;
			c=rand()%6+33;
			printf("%c %c %c\n",a,b,c);
			if(a==b&&b==c){
				printf("Jackpot!\n");
			}else{
				if(a==b || b==c || a==c){
					printf("아쉽네요.\n");
				}else{
					printf("운이없네요.\n");
				}
			}
		}else if(start==2){
			printf("안녕히가세요.");
			break;
		}else if(start==3){
			printf("게임을 시작하면 슬롯머신이 돌아갑니다.\n세개의 기호가모두같으면 Jackpot!\n");
		}else{
			printf("잘못 입력하셨습니다.\n");
		}
	}
}
