#include <stdio.h>
#include <sys/types.h>
#include <unistd.h> 

int main() { 
    pid_t pid = fork();
    printf("PID: %d\n", pid);
    return 0; 
}
