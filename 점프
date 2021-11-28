#include <stdio.h>
#include <windows.h>
void gotoxy(int x,int y);
void jump();
void CursorView();
int main(){
	CursorView();
	int cx=10,cy=10,jump=0,jumplevel=0;
	while(1){
		gotoxy(0,11);
		printf("------------------------------------------------------------------------------------------------------------------------");
		gotoxy(cx,cy);
		printf("†");
		if(GetAsyncKeyState(VK_LEFT)){
			cx--;
		}
		if(GetAsyncKeyState(VK_RIGHT)){
			cx++;
		}
		if(GetAsyncKeyState(VK_UP)){
			jump=1;
		}
		if(jump==1){
			if(jumplevel==0){
				cy--;
			}if(jumplevel==1){
				cy--;
			}if(jumplevel==2){
				cy--;
			}if(jumplevel==3){
				cy++;
			}if(jumplevel==4){
				cy++;
				
			}
			jumplevel++;
			if(jumplevel==5){
				cy++;
				jump=0;
				jumplevel=0;
			}
			
		}
		system("cls");
	}
}
void gotoxy(int x,int y){
	COORD Pos = { x , y  };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Pos);
}
void CursorView(){
    CONSOLE_CURSOR_INFO cursorInfo = { 0, };
    cursorInfo.dwSize = 1; //커서 굵기 (1 ~ 100)
    cursorInfo.bVisible = FALSE; //커서 Visible TRUE(보임) FALSE(숨김)
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursorInfo);
}
