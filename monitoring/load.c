#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main(){
    char cmd[50];
    strcpy(cmd,"mysql -u[user] -p[password] [table] < ./go.sql");
    system(cmd);
    return 0;
}



