#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct A
{
	char i;
	void func()
	{
		printf("Hello, World!\n");
	}
};
struct B : A
{
	char c;
	void func2()
	{
		printf("Life, the Universe, and Everything!\n");
	}
};
int main()
{
	B b;
	printf("b.i == %i\n", b.i);
	printf("b.i == %i\n", b.c);
	return 0;
}







