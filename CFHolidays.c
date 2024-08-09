// Holidays                 https://codeforces.com/contest/670/problem/A
#include <stdio.h>

int main(){
    int n;
    int max = 0;
    int min = 0;
   scanf("%i",&n);
   if (n >= 2 && n <= 6){
    max=2;
    if(n==6){
            min+=1;
        }else{
            min+=0;
        }
   }else if (n==1)
   {
    max=1;
    min=0;
   }else if (n==7)
   {
    max = 2;
    min = 2;
   }
   
   
   
   if(n%7==0){
    max = (n/7)*2;
    min = max;
   }else if ((n%7!=0) && (n>7))
   {
    int k=n%7;
    max = ((n-k)/7) * 2;
    min = max;
    if(k>=2){
        max+=2;
        if(k==6){
            min+=1;
        }else{
            min+=0;
        }
    }
    else if (k==1)
    {
        max+=1;
    }else{
        max+=2;
    }
    
   }
   
   printf("%i %i",min, max);
   
   };