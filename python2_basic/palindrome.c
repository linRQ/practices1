#include <string.h>

//检测是否是回文
int is_palindrome(char *text){
    int i, n=strlen(text);
    for(i=0; i<=n/2; ++i){
        if(text[i] != text[n-i-1])
            return 0;
    }
    return 1;
}