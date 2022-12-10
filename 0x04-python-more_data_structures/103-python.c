#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print information about a PyListObject
 *
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	PyListObject *l = (PyListObject *)p;
	Py_ssize_t i, size, allocated;
	PyObject **obj_list;

	size = l->ob_base.ob_size;
	allocated = l->allocated;
	obj_list = l->ob_item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, (obj_list[i])->ob_type->tp_name);
		if (strcmp(obj_list[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(obj_list[i]);
	}
}

/**
 * print_python_bytes - print information about a PyBytesObject
 *
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *b = (PyBytesObject *)p;
	Py_ssize_t i, size, bytes_to_print;
	const char *type;
	char *str;

	size = b->ob_base.ob_size;
	bytes_to_print = size < 10 ? size + 1 : 10;
	type = b->ob_base.ob_base.ob_type->tp_name;
	str = b->ob_sval;

	printf("[.] bytes object info\n");
	if (strcmp(type, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes:", bytes_to_print);
	for (i = 0; i < bytes_to_print; i++)
		printf(" %02x", str[i]);
	printf("\n");
}
