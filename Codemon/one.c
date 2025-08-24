#include <stdio.h>

int main(){

    int n, s;
    int sum;
    int missing; 
    scanf("%d %d", &n, &s);

    for(int i=0; i<n; i++){
        sum = sum+i+1;
    }
    missing = sum - s;
    if(missing==0){
        printf("-1");
        return 0;
    }
    printf("%d", missing);

    return 0;
}