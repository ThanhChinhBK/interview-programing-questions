#include <stdio.h>

void update(int *a,int *b) {
  int tmp = *a;
  *a = *a + *b ;
  *b = tmp > *b ? tmp - *b : *b - tmp;
}

int main() {
  int a, b;
  int *pa = &a, *pb = &b;
  
  scanf("%d %d", &a, &b);
  update(pa, pb);
  printf("%d\n%d", a, b);
  
  return 0;
}
