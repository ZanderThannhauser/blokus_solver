#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct A
{
	double d;
	int i;
	void func()
	{
		printf("Hello, World!\n");
	}
};
struct B : A
{
	double b;
	void func2()
	{
		printf("Life, the Universe, and Everything!\n");
	}
};
int main()
{
	A a;
	a.d = 3.14;
	a.i = -1;
	printf("a.d == %f\n", a.d);
	printf("a.i == %i\n", a.i);
	a.func();
	B b;
	b.d = 3.14;
	b.i = -1;
	printf("b.d == %f\n", b.d);
	printf("b.i == %i\n", b.i);
	b.func();
	b.func2();
	return 0;
}







