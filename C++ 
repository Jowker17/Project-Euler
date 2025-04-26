//10001th prime.cpp

#include<iostream>
#include <chrono>
using namespace std;
using namespace chrono;

// let's first create a function
bool isPrime(int x){
  if (x < 2) return false;
  for (int i=2;i*i <= x;i++)
  {
     if (x % i==0)
     {
         return false;
     }
  }   
  return true;
}  
//it returns a Boolean value
int main(){
   auto start =
  chrono::high_resolution_clock::now();
//starting time
   int counter = 0;
   int k = 1;
   while (counter!=10001)
   {
     k++;
     if (isPrime(k)) counter++;
   }  
   auto end = 
    chrono::high_resolution_clock::now();
//ending time
   chrono::duration<double>duration = end-start;
//Program's duration
   cout<<k<<endl<<"time: "<<duration.count()<<" ms";
   return 0;
}