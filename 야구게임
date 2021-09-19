#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int main(){
	//야구게임만들기
	//노가다...... 
	int a1,b1,c1,a2,b2,c2,s=0,b=0,o=0,start;
	srand(time(NULL));
	
	while(1){
		s=0;b=0;o=0;
		printf("[Baseball Game]\n");
		printf("숫자를입력후 'Enter'키를 누르세요.\n");
		printf("1.게임시작 // 2.나가기 // 3.게임설명>>");
		scanf("%d",&start);
		if(start==1){
			a1=rand()%9+1;
			b1=rand()%10;
			c1=rand()%10;
			printf("숫자를 3개입력하세요.\n");
			for(int r=1,p=1;r==1;p++){
				s=0;b=0;o=0;
				printf("백의자리:");
				scanf("%d",&a2);
				printf("십의자리:");
				scanf("%d",&b2);
				printf("일의자리:");
				scanf("%d",&c2);
				if(a1==a2){
					s++;
				}
				if(b1==b2){
					s++;
				}
				if(c1==c2){
					s++;
				}
				if(a1!=a2&&b1!=b2&&a1==b2){
					b++;
				}
				if(b1!=b2&&a1!=a2&&b1==a2){
					b++;
				}
				if(b1!=b2&&c1!=c2&&b1==c2){
					b++;
				}
				if(a1!=a2&&c1!=c2&&a1==c2){
					b++;
				}
				o=3-s-b;
				printf("%d S\n%d B\n%d O\n",s,b,o);
				if(s==3){
					r=0;
					printf("%d번만에 성공하셨네요.\n",p);
					printf("정답은%d%d%d이었네요.",a1,b1,c1);
					printf("잘하셨어요!\n");
				}
			}
		}else if(start==2){
			printf("안녕히가세요.");
			break;
		}else if(start==3){
			printf("컴퓨터가 세자리수의수를 정합니다.\n");
			printf("숫자를세개말했을때 자리수와 숫자모두같으면 스트라이크(S),숫자는 맞아지만 자리수가틀리면 볼(B),");
			printf("숫자까지틀리면 아웃(O)입니다.\n3스트라이크면 성공!\n");
		}else{
			printf("잘못 입력하셨습니다.\n");
		}
	}
}
