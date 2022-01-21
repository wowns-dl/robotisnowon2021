//[C/C++ game] very simple google dinosaur.
//BlockDMask. 
//#include <stdio.h>
//#include <unistd.h>
//#include <windows.h>
//int main(){
//	while(1){
//	printf("???");
//	sleep(0.5);
//;	system("cls");
//	sleep(0.5);
// }
//}



#include <stdio.h>
#include <windows.h>
void gotoxy(int x,int y);
int main(){
	int x=1,y=1;
	gotoxy(x,y);
	while(1){
		if(GetAsyncKeyState(VK_UP)){
			y--;
		}
		if(GetAsyncKeyState(VK_DOWN)){
			y++;
		}
		if(GetAsyncKeyState(VK_LEFT)){
			x--;
		}
		if(GetAsyncKeyState(VK_RIGHT)){
			x++;
		}
		system("cls");
		gotoxy(x,y);
		printf("★");
	}
}

void gotoxy(int x,int y){
	COORD Pos = { x - 1, y - 1 };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Pos);
}
/*system("mode con:cols=100 lines=10");  콘솔창크기
system("color 4(배겨2");  콘솔창색상 
SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), 1);  폰트색상 
 검정			 0
 어두운 파랑	 1
 어두운 초록	 2
 어두운 하늘	 3
 어두운 빨강	 4
 어두운 보라	 5
 어두운 노랑	 6
 회색			 7
 어두운 회색	 8
 파랑	 		 9
 초록	 		 10
 하늘	 		 11
 빨강			 12
 보라	  		 13
 노랑	 		 14
 하양			 15*/
const
