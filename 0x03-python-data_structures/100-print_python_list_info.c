#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print info about a python list
 *
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	int i, size, allocated;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
