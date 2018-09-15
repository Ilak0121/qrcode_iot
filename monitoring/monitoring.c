#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>

#include<sys/types.h>
#include<sys/stat.h>

int main(){
    char Filepath[10];
    time_t* time;
    char buf1[100]={0,};
    char buf2[100]={0,};

    struct stat FileAttrib;
    FILE* fp = NULL; 

    strcpy(Filepath,"./go.sql"); //file path of monitoring
    
    if(!(fp=fopen("./log.txt","r"))){
        fprintf(stdout,"log.txt open error");
    }else{ 
        fgets(buf1,100,fp);
        printf("buf1 : %s",buf1);
    }
    fclose(fp);//read file stream close

    if(!(fp=fopen("./log.txt","w"))){ //write file stream open
        fprintf(stdout,"file open error\n");
    }

    if(stat(Filepath, &FileAttrib) != 0)
        printf("File Error Message = %s\n",strerror(errno));
    else{
        
        time = (time_t *)&FileAttrib.st_atime;
        time = (time_t *)localtime(time);
        strcpy(buf2,asctime(time));
        printf("buf2 : %s",buf2);
    }

    if(strcmp(buf1,buf2)){
        printf("diff!!\n");
        fprintf(fp,"%s",buf2);
    }else{
        printf("same!!\n");
        fprintf(fp,"%s",buf2);
    }
            
    if(fclose(fp))
        perror("so sad\n");
    return 0;
}
