#include <stdio.h>
#include <Python.h>
/**
 * print_python_float - prints python floating points
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOs_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}
/**
 * print_python_bytes - prints python bytes
 * @p: PyObjeect
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i = 0, j = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	i = PyBytes_Size(p);
	printf("  size: %zd\n", i);
	str = (assert(PyBytes_check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", i < 10 ? i + 1 : 10);
	while (j < i + 1 && j < 10)
	{
		printf("  %02hhx", str[j]);
		j++;
	}
	print("\n");
}
/**
 * print_python_list - print python list
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i = 0;
	PyObject *obj;
	int j = 0;

	fflush(stdout);
	printf("[.] Python list info\n");
	if (PyBytes_CheckExact(p))
	{
		i = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", i);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (j < i)
		{
			obj = PyList_GET_ITEM(p, j);
			printf("Element %d: %s\n", j, obj->ob_type->tp_name);
			if (PyBytes_Check(obj))
				print_python_bytes(obj);
			else if (PyFloat_Check(obj))
				print_python_float(obj);
			j++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
