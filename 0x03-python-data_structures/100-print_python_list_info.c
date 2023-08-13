#include <object.h>
#include <listobject.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	long int data = PyList_Size(p);
	int x;
	PyListObject *item = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", data);
	printf("[*] Allocated = %li\n", item->allocated);
	for (x = 0; x < data; x++)
		printf("Elemrnt %x: %s\n", x, Py_TYPE(item->ob_item[x])->tp_name);
}
