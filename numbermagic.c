#include<stdio.h>
#include<conio.h>
int generate(void);
int fun(int);
main()
{
int i,a,r;

printf("\n\nWelcome!");
printf("\nPress any key to continue....");
getch();
printf("\n\nJust think a number between 1 and 100 in your mind");
printf("\nThink on one");
printf("\nDo not enter that number");
printf("\n\nI will find that number on your mind....");
printf("\n\nPress any key to continue...");
getch();
printf("\nBy Just answering few questions....");
printf("\n\nIf your number is present in the numbers");
printf("\n\nshown on your screen,Then press P and if not present ");
printf("then press N ");
printf("\nBut please be honest while entering the answer...");
printf("\n\nPress any key to continue...");
getch();
r=generate();
if(r==0)
{
  printf("\nYou didn't think of any number between 1 and 100");
  printf("\nSo try again...");
}
else
{
printf("\nYour number is %d",r);
printf("\nSurprised! But friends it is not a magic,");
printf("\nit just involves some mathematical computation....");
printf("\nso guys just try to find out the method.");
}
getch();
}
int generate()
{
int a,i,j,f,num[6],n,r=0;
char ch[6];
for(j=0;j<=5;j++)
{
  f=fun(j);
  for(i=1;i<=100;i++)
  {
   f=fun(j);
   printf(" %d",f);
   a=i & f;
   if(a==f)
   printf(" %d",i);
  }
  printf("\n\n  Let me remind you if the number is present then");
  printf("\n press P otherwise press N");
  printf("\nEnter your answer: ");
  ch[j]=getche();
  printf("\nPress any key to continue....");
  if(ch[j]=='p' || ch[j]=='P')
  {
   num[j]=1;
   n=fun(j);
   r=r+n;
  }
  else
  num[j]=0;
  getch();
}
for(j=5;j>=0;j--)
{

if(ch[j]=='p' || ch[j]=='P')
num[j]=1;
else
num[j]=0;
}
return r;
}
int fun(int j)
{
if(j==0)
return 1;
else
return (2*fun(j-1));
}
