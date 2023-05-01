#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - an infite function
 * Prevents parent from exiting
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program integration
 * Generates zombie
 * Return: 0
 */
int main(void)
{
	int pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}
	infinite_while();
	return (0);
}

