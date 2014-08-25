#include <stdio.h>
#include <stdlib.h>
#include <termios.h>
#include <unistd.h>
#include <time.h>
int getch(void)
{
struct termios oldattr, newattr;
int ch;
tcgetattr( STDIN_FILENO, &oldattr );
newattr = oldattr;
newattr.c_lflag &= ~( ICANON | ECHO );
tcsetattr( STDIN_FILENO, TCSANOW, &newattr );
ch = getchar();
tcsetattr( STDIN_FILENO, TCSANOW, &oldattr );
return ch;
}

int main()
{   srand(time(NULL));
    char choice=' ';
    int posx,posy,i,j;
    int tarx,tary,moves=0;
    int dx,dy,x,y;
    printf("Size: x=");scanf("%d",&x);
    printf("      y=");scanf("%d",&y);
    char board[y][x];
    for(i=0;i<y;i++)
        for(j=0;j<x;j++)
            board[i][j]='x';


    tarx=rand()%x;tary=rand()%y;
    posx=rand()%x;posy=rand()%y;
    do  {
            posx=rand()%x;posy=rand()%y;
        }while(tarx==posx && tary==posy);
    do{system("clear");
    for(i=0;i<y;i++)
    {   for(j=0;j<x;j++)
            if (posx==j && posy==i)printf("H ");
            else printf("%c ",board[i][j]);
        printf("\n");
    }
    if(posx==tarx && posy==tary)break;
    dx=posx-tarx;
    dy=posy-tary;
    if(dx<0)dx*=-1;
    if(dy<0)dy*=-1;
    printf("move(w,s,a,d)(end=x)\n\nsize=%dx%d, distance=%d, moves=%d",x,y,dx+dy,moves);choice=getch();moves++;
    switch(choice)
    {
        case 'w': if(posy!=0)posy--;break;
        case 's': if(posy!=y-1)posy++;break;
        case 'a': if(posx!=0)posx--;break;
        case 'd': if(posx!=x-1)posx++;break;
        case 'x': break;
    }printf("\n");}while(choice!='x');
    if(posx==tarx && posy==tary)printf("\n\n!! YOU WIN !!\n");

    return 0;
}
