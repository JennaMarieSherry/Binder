{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# $\\color{Green}{\\text{Cheat Sheet}}$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Functions}}$\n",
    "```python\n",
    "+     # addition (same variable type)\n",
    "-     # subtraction\n",
    "*     # multiplication\n",
    "/     # division\n",
    "**    # exponentiation\n",
    "==    # equals\n",
    "!=    # does not equal\n",
    ">     # greater than\n",
    ">=    # greater than or equal to\n",
    "<     # less than \n",
    "<=    # less than or equal to \n",
    "=     # assigning variables\n",
    "+     # concatenating variables of same type\n",
    ",     # to separate values of different datatype\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Commands and Modulators}}$\n",
    "```python\n",
    "print ()\n",
    "type ()\n",
    "input ()\n",
    "\n",
    "str ()\n",
    "int ()\n",
    "float ()\n",
    "\n",
    "del \n",
    "and\n",
    "or\n",
    "\n",
    "reset \n",
    "\n",
    "list_name[x:y:z]            # range x to y, count by z\n",
    "list_name.append(x)         # appends x to list_name\n",
    "input(\"Input\").upper        # capitalizes input string\n",
    "\", \".join(l)                # joins list by previous\n",
    "(list_name, end=\"\")         # ends list with \" \"\n",
    "(list_name, sep=\"\")         # separates list values by \" \"\n",
    "(x, \"\\n\", y)                # prints new line between vars\n",
    "(x, \"\\t\", y)                # prints tab between vars\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Coditionals & Booleans, Loops}}$\n",
    "```python\n",
    "True\n",
    "False\n",
    "break\n",
    "\n",
    "if (condition_1):\n",
    "    function_1\n",
    "    break\n",
    "elif (condition_2):\n",
    "    function_2\n",
    "else:\n",
    "    function_3\n",
    " \n",
    "    \n",
    "    \n",
    "while (condition):\n",
    "    function\n",
    "\n",
    "   \n",
    "    \n",
    "for variable in range (x, y):\n",
    "    function\n",
    "\n",
    "for element in list_name:\n",
    "    function\n",
    "\n",
    "    \n",
    "    \n",
    "try:\n",
    "    val = function_1\n",
    "    if (val condition):\n",
    "        function_2\n",
    "    else:\n",
    "        function_3\n",
    "except ValueError:\n",
    "    function_4\n",
    "    ```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Libraries}}$\n",
    "```python\n",
    "import library as rename\n",
    "from library import *  \n",
    "\n",
    "numpy           # number library\n",
    "    sqrt()      # square root (as numpy.sqrt)\n",
    "    \n",
    "random          # random library\n",
    "    randint()   # random integer (as random.randint)\n",
    "    sample()    # random sample list (range(x, y), number)\n",
    "    \n",
    "sympy           # symbolic mathematics\n",
    "    isprime()   # checks prime number (as sympy.isprime)\n",
    "```\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
