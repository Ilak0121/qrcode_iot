#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>

#include<sys/types.h>
#include<sys/stat.h>

int main(int argc, char *argv[]){
    time_t time;
    char buf[100];
    struct stat FileAttrib;
    if(argc <=1){
        printf("Argument missing! \n");
        exit(10);
    }
    if(stat(argv[(argc -1)], &FileAttrib)<0)
        printf("File Error Message = %s\n",strerror(errno));
    else{
        time = FileAttrib.st_atime;
        strcpy(buf,asctime(time));
        printf("Timestamp : %s\n",buf);
    }
    return 0;
}
