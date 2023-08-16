#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints python byte info
 * @p: object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	char *i;
	long int j, k, l;

	printf("[.] bytes object info\n");
	if (!PyBytes_check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	j = ((PyVarObject *)(p))->ob_size;
	i = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", j);
	printf("  trying string: %s\n", i);
	if (j >= 10)
		l = 10;
	else
		l = j + 1;
	printf("  first %ld bytes:", limit);
	for (x = 0; x < l; x++)
		if (i[x] >= 0)
			printf("  %02x", i[x]);
		else
			printf("  %02x", 256 + i[x]);
	printf("\n");
}

/**
 * print_python_bytes - prints python list info
 * @p: object
 * Return: null
 */
void print_python_bytes(PyObject *p)
{
	long int i, j;
	PyListObject *k;
	PyObject *l;

	x = ((PyVarObject *)(p))->ob_size;
	y = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", x);
	printf("[*] Allocated = %ld\n", y->allocated);

	for (z = 0; z < x; z++)
	{
		l = ((PyListObject *)p)->ob_item[z];
		printf("Element %ld: %s\n", z, ((x)->ob_type)->tp_name);
		if (PyBytes_Check(l))
			print_python_bytes(l);
	}
}
