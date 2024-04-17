#include <stdio.h>

int main(void) { 
    int x =2;
    int y =5;
    printf("antes x = %d\n",x,y);
    intercambio(&x,&y);
    printf("despues x =%d\n",x,y);
 return 0;
    
}
void intercambio{
   int temp;
   temp=*b;
   *b=*a;
   *a=temp;
 }