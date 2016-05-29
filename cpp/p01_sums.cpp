// Find the sum of all the numbers less than 1000 which are multiples
// of either 3 or 5
// O(sum_limit) solution

#include<iostream>

int main(){
  int sum_limit = 1000;
  int res_sum = 0;

  for (int i = 2; i < sum_limit; i++){
    if (i % 3 == 0 || i % 5 == 0){
      res_sum += i;
    }
  }
  std::cout << "Sum is: " << res_sum;

  return 0;
}
