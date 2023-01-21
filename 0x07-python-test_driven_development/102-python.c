#include "Python.h"

/**
 * print_python_string - print information about a python string object
 *
 * @p: PyObject
 */
void print_python_string(PyObject *p)
{
	PyUnicodeObject *u = (PyUnicodeObject *)p;
	const char *type = p->ob_type->tp_name;
	unsigned int ascii = u->_base._base.state.ascii;
	unsigned int compact = u->_base._base.state.compact;
	Py_ssize_t length = u->_base._base.length;

	printf("[.] string object info\n");
	if (strcmp(type, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	printf("  type: %s%s\n",
			compact ? "compact " : "",
			ascii ? "ascii" : "unicode object");
	printf("  length: %ld\n", length);
	printf("  value: %s\n", PyUnicode_AsUTF8(p));
}
