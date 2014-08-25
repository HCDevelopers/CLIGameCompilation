#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int createboard();
int x_player();
int o_player();
int winner();
int check();
int win=0,wrong_X=0,wrong_O=0,chk=0;

char namex[30];
char nameo[30];
int xpos[3][3];
int opos[3][3];
int pos_marked[3][3];

main()
{
int i,ch,j;
char ans;

printf("\n\t\t\t\tTIC TAC TOE");
printf("\n\t\t\t\t");
for(i=1;i<=11;i++)
{
  
  printf("*");
}
do
{
  
  printf("\n\t\t\t\tTIC TAC TOE");
  printf("\n\t\t\t\t");
  for(i=1;i<=11;i++)
  {
  
   printf("*");
  }
  printf("\n1.Start The Game");
  printf("\n2.Quit The Game");
  printf("\nEnter your choice(1-2) : ");
  scanf("%d",&ch);
  switch(ch)
  {
   case 1:
    chk=0;
    win=0;
    for(i=1;i<=3;i++)
    {
     for(j=1;j<=3;j++)
     {
      xpos[i][j]=0;
      opos[i][j]=0;
      pos_marked[i][j]=0;
     }
    }
    printf("\n\n");
    
    printf("\nEnter the name of the player playing for \'X\': ");
    fflush(stdin);
    gets(namex);
    printf("\nEnter the name of the player playing for \'O\': ");
    fflush(stdin);
    gets(nameo);
    createboard();
    for(;;)
    {
     if(win==1)
      break;
     check();
     if(chk==9)
     {
      printf("\n\t\t\tMATCH DRAWS!!");
      printf("\nPress any key....");
      break;
     }
     else
      chk=0;
     printf("\nTURN FOR %s:",namex);
     x_player();
     do
     {
      if(wrong_X!=1)
       break;
      wrong_X=0;
      printf("\nTURN FOR %s:",namex);
      x_player();
     }while(wrong_X==1);
     check();
     if(chk==9)
     {
      printf("\n\t\t\tMATCH DRAWS");
      printf("\nPress any key....");
      break;
     }
     else
      chk=0;
     printf("\nTURN FOR %s:",nameo);
     o_player();
     do
     {
      if(wrong_O!=1)
       break;
      wrong_O=0;
      printf("\nTURN FOR %s:",nameo);
      o_player();
     }while(wrong_O==1);

     }
    createboard();
    if(win!=1)
    {
     printf("\n\t\t\tMATCH DRAWS!!");
     printf("\nPress any key.......");
    }
    getch();
    break;
   case 2:
    printf("\n\n\n\t\t\tThank You For Playing The Game.");
    printf("\n\t\t\t###############################");
    getch();
    exit(1);
    break;
  }
  printf("\nWant To Play(Y/N) ? ");
  fflush(stdin);
  scanf("%c",&ans);
}while(ans=='y' || ans=='Y');
getch();
}


int createboard()
{
int i,j;

printf("\n\t\t\t\tTIC TAC TOE BOARD");
printf("\n\t\t\t\t*****************");
printf("\n\n\n");
printf("\n\t\t\t    1\t      2\t        3");
for(i=1;i<=3;i++)
{
  printf("\n \t\t\t _____________________________");
  printf("\n \t\t\tº\t  º\t   º\t     º");
  printf("\n\t\t%d\t",i);
  for(j=1;j<=3;j++)
  {

   if(xpos[i][j]==1)
   {
    printf("    X");
    printf("     ");
   }
   else if(opos[i][j]==1)
   {
    printf("    O");
    printf("     ");
   }
   else
   {
    printf("          ");
    continue;
   }
  }
  printf("\n\t\t\tº\t  º\t   º\t     º");
}
printf("\n\t\t\t------------------------------");
winner();
}


int x_player()
{
int row,col;
if(win==1)
  return win;
printf("\nEnter the row no. : ");
fflush(stdin);
scanf("%d",&row);
printf("Enter the column no. : ");
fflush(stdin);
scanf("%d",&col);
if(pos_marked[row][col]==1 || row<1 || row>3 || col<1 || col>3)
{
  printf("\nWRONG POSITION!! Press any key.....");
  wrong_X=1;
  getch();
  createboard();
}
else
{
  xpos[row][col]=1;
  pos_marked[row][col]=1;
  createboard();
}
}
int o_player()
{
int row,col;
if(win==1)
  return win;
printf("\nEnter the row no. : ");
scanf("%d",&row);
printf("Enter the column no. : ");
scanf("%d",&col);
if(pos_marked[row][col]==1 || row<1 || row>3 || col<1 || col>3)
{
  printf("\nWRONG POSITION!! Press any key....");
  wrong_O=1;
  getch();
  createboard();
}
else
{
  opos[row][col]=1;
  pos_marked[row][col]=1;
  createboard();
}
}
int winner()
{
int i;
for(i=1;i<=3;i++)
{
  if(xpos[i][1]==1 && xpos[i][2]==1 && xpos[i][3]==1)
  {
   win=1;
   printf("\n\nRESULT: %s wins!!",namex);
   printf("\nPress any key............");
   return win;
  }
}
for(i=1;i<=3;i++)
{
  if(xpos[1][i]==1 && xpos[2][i]==1 && xpos[3][i]==1)
  {
   win=1;
   printf("\n\nRESULT: %s wins!!",namex);
   printf("\nPress any key............");
   return win;
  }
}
if(xpos[1][1]==1 && xpos[2][2]==1 && xpos[3][3]==1)
{
  win=1;
  printf("\n\nRESULTL: %s wins!!",namex);
  printf("\nPress any key......");
  return win;
}
else if(xpos[1][3]==1 && xpos[2][2]==1 &&xpos[3][1]==1)
{
         win=1;
  printf("\n\nRESULT: %s wins!!",namex);
                printf("\nPress any key.....");
  return win;
}

        for(i=1;i<=3;i++)
{
  if(opos[i][1]==1 && opos[i][2]==1 && opos[i][3]==1)
  {
   win=1;
   printf("\n\nRESULT: %s wins!!",nameo);
                        printf("\nPress any key.....");
   return win;
  }
}
for(i=1;i<=3;i++)
{
  if(opos[1][i]==1 && opos[2][i]==1 && opos[3][i]==1)
  {
   win=1;
   printf("\n\nRESULT: %s wins!!",nameo);
            printf("\nPress any key.....");
   return win;
  }
}
if(opos[1][1]==1 && opos[2][2]==1 && opos[3][3]==1)
{
  win=1;
  printf("\n\nRESULT: %s wins!!",nameo);
  printf("\nPress any key.....");
  return win;
}
else if(opos[1][3]==1 && opos[2][2]==1 &&
opos[3][1]==1)
{
         win=1;
  printf("\n\nRESULT: %s wins!!",nameo);
                printf("\nPress any key.....");
  return win;
}
}
int check()
{
int i,j;
for(i=1;i<=3;i++)
{
  for(j=1;j<=3;j++)
  {
   if(pos_marked[i][j]==1)
    chk++;
   else
    continue;
  }
}
}
