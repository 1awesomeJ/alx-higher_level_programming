#include <stdio.h>
#include "Python.h"

void print_python_list_info(PyObject *p)
{	
	int i;
	PyListObject *k;
		k = (PyListObject*)p;
	printf("[*] Size of the Python List = %ld\n", k->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", k->allocated);
	for (i = 0; i < k->ob_base.ob_size; i++)
	       printf("Element %d: %s\n", i, k->ob_item[i]->ob_type->tp_name);	

}
