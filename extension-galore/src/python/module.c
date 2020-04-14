#include <Python.h>
#include "primes.h"

static PyObject*
primes(PyObject *module, PyObject *args)
{
    int n_primes = 0;

    if (!PyArg_ParseTuple(args, "i", &n_primes)) {
        return NULL;
    }
    n_primes = n_primes > 10000 ? 10000 : n_primes;

    int *primes = (int*) malloc(n_primes * sizeof(int));

    primes_c(n_primes, primes);

    PyObject *result = PyList_New(n_primes);
    for(int i=0; i < n_primes; i++)
        PyList_SetItem(result, i, PyLong_FromLong(primes[i]));

    free(primes);

    return result;
}

static PyMethodDef myModule_methods[] = {
    {
        "primes",
        (PyCFunction) primes,
        METH_VARARGS,
        "a routine for finding prime numbers"
    }, {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "cpp",
        NULL,
        -1,
        myModule_methods,
};


PyMODINIT_FUNC
PyInit_cpp(void)
{
    return PyModule_Create(&moduledef);
}

