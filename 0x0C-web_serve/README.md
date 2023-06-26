# 0x0C. Web server
[img](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)
In this project, some of the tasks will be graded on 2 aspects:
1. Is your `web-01` server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default.`

But my answer file would contain:
```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```
As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://intranet.alxswe.com/rltoken/9I0WufjKdW3TZA2EVrGnlQ), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the `root` user, you do not need to use the `sudo` command.
A good Software Engineer is a [lazy Software Engineer](https://intranet.alxswe.com/rltoken/sRY__axKNHhNW0SVmsUC_A).

[img](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

Tips: to test your answer Bash script, feel free to reproduce the checker environment:
- start a Ubuntu 16.04 sandbox
- run your script on it
- see how it behaves

## Resources
### Read or watch:

- [How the web works](https://intranet.alxswe.com/rltoken/6TI3HiyFdwrbXWKVF24Gxw)
- [Nginx](https://intranet.alxswe.com/rltoken/vkVMGlaf39j2DWAQWzo6EA)
- [How to Configure Nginx](https://intranet.alxswe.com/rltoken/zKrpVxWuUHVdW4URAjdFbw)
- [Child process concept page](https://intranet.alxswe.com/rltoken/Ar18u5sRis1fkvkVgzdcqg)
- [Root and sub domain](https://intranet.alxswe.com/rltoken/xi3peVqYl02PfpHHHlCtxQ)
- [HTTP requests](https://intranet.alxswe.com/rltoken/sBrrP4EAmI3NoYjIgZrUhw)
- [HTTP redirection](https://intranet.alxswe.com/rltoken/Eaa4ZuKvye941hTkP8VlBQ)
- [Not found HTTP response code](https://intranet.alxswe.com/rltoken/eJSp2QFTY6jqqNtz8OVDEw)
- [Logs files on Linux](https://intranet.alxswe.com/rltoken/7WMNY5CWD-CBrxmQrdmfPg)

### For reference:
- [RFC 7231 (HTTP/1.1)](https://intranet.alxswe.com/rltoken/BGa6RrS0dnM6EdBGS_ZDUw)
- [RFC 7540 (HTTP/2)](https://intranet.alxswe.com/rltoken/IZ2fyYn1qNZ9RXXsg5vG1g)


### man or help:
- scp
- curl

### General
- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests
### DNS
- What DNS stands for
- What is DNS main role
### DNS Record Types
- A
- CNAME
- TXT
- MX
