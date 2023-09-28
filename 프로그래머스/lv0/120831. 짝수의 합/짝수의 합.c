#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int count = 0;

    for(int answer = 0; answer <= n; answer++) {
        if (answer % 2 == 0) {
            count = count + answer;
        }
    }
    
    return count;
}