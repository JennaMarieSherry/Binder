{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# $\\color{Green}{\\text{Notes}}$\n",
    "\n",
    "Introduction to Python with Professor Dan Uken\n",
    "\n",
    "February 27th, 2018\n",
    "March 6th, 2018 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date and time last edit: \n",
      "2019-03-06 23:21:49\n"
     ]
    }
   ],
   "source": [
    "from datetime import *\n",
    "now = datetime.now()\n",
    "print (\"Date and time last edit: \")\n",
    "print (now.strftime (\"%Y-%m-%d %H:%M:%S\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# $\\color{Green}{\\text{Introduction}}$\n",
    "\n",
    "February 27th, 2018\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Printing to Screen}}$\n",
    "\n",
    "Use *print* command, and *execute* code by pressing *shift + enter* \n",
    "\n",
    "When printing strings, put information within quotation marks. \n",
    "```python\n",
    "print (\"Hello world!\")        output [Hello world!]\n",
    "print (1 +2 )                 output [3]\n",
    "print (1 + 2, 2 * 3)          output [3 6]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Calculations}}$\n",
    "\n",
    "To conduct calculations, we do not use an $\\color{purple}{\\text{=}}$ sign. Treat Python like a calculator and input the values, then *execute* command. \n",
    "\n",
    "If you want to conduct calculations that involve equality (such as to test \"true\" or \"false\" on equation $\\color{green}{\\text{5}}$ $\\color{purple}{\\text{+}}$ $\\color{green}{\\text{2}}$ $\\color{purple}{\\text{=}}$ $\\color{green}{\\text{9}}$), do not use $\\color{purple}{\\text{=}}$, as that is reserved for variable assignment. To indicate equity, use $\\color{purple}{\\text{==}}$.\n",
    "\n",
    "Note that division returns a *float* \n",
    "```python\n",
    "9 + 3                         output [12]\n",
    "9 - 3                         output [6] \n",
    "9 * 3                         output [27] \n",
    "9 / 3                         output [3.0]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Checking Data Type}}$\n",
    "\n",
    "The type command is used to determine that datatype a variable is\n",
    "\n",
    "```python\n",
    "type (variable)\n",
    "```\n",
    "\n",
    "The type command will return either int, float, or string\n",
    "\n",
    "```python\n",
    "int( )    # numerical integer\n",
    "float( )  # numerical floating decimal\n",
    "str( )    # non-numerical text\n",
    "\n",
    "type (variable_name)          output [int]\n",
    "type (\"word\")                 output [str]\n",
    "type (5.0)                    output [float] \n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Variable Assignment}}$\n",
    "Variable names cannot include spaces (instead use underscore), and cannot be the name of a Python function like *print*. These names are assigned to specific values using an $\\color{purple}{\\text{=}}$ equals sign. It is good practice to *print* your variable after assigning to make sure your assignment was valid. As variable names are assignments and not strings, quotation marks are not needed. \n",
    "\n",
    "Use variable assignment to store variable values so that you do not need to keep re-typing information.\n",
    "\n",
    "```python\n",
    "variable_name = 15\n",
    "print (variable_name)         output [15]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can also create a variable from existing ones\n",
    "\n",
    "```python\n",
    "x = 2\n",
    "y = 3\n",
    "z = x + y \n",
    "print (z)                     output [5]\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Variables can also store *strings* as long as you put your string in approproiate quotations\n",
    "\n",
    "```python\n",
    "name = \"Jenna\"\n",
    "```\n",
    "\n",
    "This is usefulfor allowing a user to input information when you execute your code - see below for more informaiton. \n",
    "\n",
    "To remove an assignment, use command \n",
    "```python\n",
    "del variable```\n",
    "\n",
    "To reset all variables, use command\n",
    "```python\n",
    "reset```\n",
    "and enter \"y\" to the prompt "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "x =2\n",
    "print (x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "del(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Once deleted, variables cannot be recovered. Proceed (y/[n])? y\n"
     ]
    }
   ],
   "source": [
    "reset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{User Input}}$\n",
    "The *input* command allows a user to input information. You must assign a variable name to the input prompt, so that user answers can be stored. It is important to remember that all values (including numeric and integer) are input as *string* datatype. In order to convert to a numerical value, you have to reassign the datatype (see below). \n",
    "\n",
    "Note: in order to print a blank line, use the *print* command and leave the space between the parentheses blank. Also be sure to include spaces within your string parameters to space out your output. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your name? Jenna\n",
      "\n",
      "Hello Jenna!\n",
      "How old are you? 26\n",
      "\n",
      "Wow, only 26? You're a baby!\n",
      "\n",
      "\n",
      "Hey guys, did you know Jenna is only 26 years old?\n"
     ]
    }
   ],
   "source": [
    "name = input(\"What is your name? \")\n",
    "\n",
    "print()\n",
    "print(\"Hello \" + name + \"!\")\n",
    "\n",
    "age = input(\"How old are you? \")\n",
    "\n",
    "print()\n",
    "print(\"Wow, only \" + age + \"? You're a baby!\")\n",
    "print ()\n",
    "print ()\n",
    "print (\"Hey guys, did you know \" + name + \" is only \" + age + \" years old?\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Assinging Datatype}}$\n",
    "As the *input* command only recognizes inputs as *string* variables, it is sometimes necessary to reassign these as numeric values. Note that only numbers or floats can be re-assigned as numeric values, as something like \"name\" would return an error\n",
    "\n",
    "First, check the type of your variable \n",
    "```python \n",
    "type (age)                     output [26]\n",
    "```\n",
    "Use the *int*, *str*, or *float* commands to **temporarily** recognize a variable as a different datatype and incorporate into a function\n",
    "```python\n",
    "int(age) + 4                   output [30]\n",
    "```\n",
    "To *permanently* alter a datatype, reassign the *variable name* as another datatype\n",
    "```python\n",
    "age = int(age)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Conditions and Booleans}}$\n",
    "**Conditions** are something that can be either *True* or *False*, such as the statement \n",
    "```python\n",
    "2 > 3                          output [False]\n",
    "5 + 4 == 9                     output [True]\n",
    "```\n",
    "**Booleans** are variables restricted by conditions; they can only have either a *True* or *False* value.\n",
    "```python\n",
    "x = 17\n",
    "y = 25\n",
    "\n",
    "z = x < y\n",
    "\n",
    "print (z)                      output [True]```\n",
    "\n",
    "**If statments** use conditions to execute conditional statements. they have the form\n",
    "```python\n",
    "if (condition):\n",
    "    \n",
    "    statements```\n",
    "Note that statements are indernted (using *tab*), which tells Python to execute the *if statement* for the hanging code. If the conditions are not met, nothing will happen."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number: 5\n",
      "\n",
      "Sorry, you lose\n"
     ]
    }
   ],
   "source": [
    "number = input(\"Please enter a number: \")\n",
    "\n",
    "number = int(number) #we need to change datatype from string to integer so we can perform numerical operations\n",
    "\n",
    "if number > 10:\n",
    "    \n",
    "    print()\n",
    "    print(\"Well done... your number is big enough!\")\n",
    "    \n",
    "if number <= 10:\n",
    "    \n",
    "    print()\n",
    "    print (\"Sorry, you lose\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Make sure to chnage your input into a numerical datatype if you wish to use it for subsequent commands or equations. \n",
    "\n",
    "Additionally, make sure to include a colon or your code will return an error message.\n",
    "\n",
    "**Else statements** apply to everything that does not come under the domain of the *if* statement... essentailly takes the place of the \"$\\color{green}{\\text{if}}$ number $\\color{purple}{\\text{<=}}$ $\\color{green}{\\text{10}}$:\" line above. The format is:\n",
    "```python\n",
    "if condition: \n",
    "    this\n",
    "else:\n",
    "    that```\n",
    "    \n",
    "**Elif statments** can be used as an intermediary condition when multiple conditions apply. It stands for *else if*, and has the following streucture: \n",
    "```python\n",
    "if condition_one:\n",
    "    this\n",
    "elif condition_two:\n",
    "    that\n",
    "else:\n",
    "    everything else```\n",
    "\n",
    "It is helpful to use the *elif* function if you want to check your conditions in chronological order. It essentially runs the *if* statement, and if true stops searching. If false, it applies the *elif* condition. If you were to use multiple *if* statements rather than *elif*, one condition may apply to multiple inputs (ex: $\\color{green}{\\text{if}}$ $\\color{purple}{\\text{>}}$ $\\color{green}{\\text{4}}$ and $\\color{green}{\\text{if}}$ $\\color{purple}{\\text{=}}$ $\\color{green}{\\text{5}}$ would both apply, where $\\color{green}{\\text{if}}$ $\\color{purple}{\\text{>}}$  $\\color{green}{\\text{4}}$ and $\\color{green}{\\text{elif}}$ $\\color{purple}{\\text{=}}$ $\\color{green}{\\text{5}}$ only the *if* condition would apply). \n",
    "\n",
    "\n",
    "We can also make compound statements by using *and* and *or* to combine simple statements: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter your name: Jenna\n",
      "Please enter your age: 26\n",
      "\n",
      "Wow, you are awesome!\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Please enter your name: \")\n",
    "\n",
    "age = input(\"Please enter your age: \")\n",
    "\n",
    "age = int(age)\n",
    "\n",
    "if (name == \"Jenna\" and age == 26):\n",
    "    \n",
    "    print()\n",
    "    print(\"Wow, you are awesome!\")\n",
    "    \n",
    "elif (name == \"Jenna\" or age == 26):\n",
    "    \n",
    "    print()\n",
    "    print(\"You've got some good qualities\")\n",
    "    \n",
    "else:\n",
    "    \n",
    "    print()\n",
    "    print(\"Meh... not going to cut it\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-------------------------------------------------*Fin*-------------------------------------------------"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# $\\color{Green}{\\text{Lecture 1}}$\n",
    "\n",
    "February 27th, 2018\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Libraries / Modules}}$\n",
    "Libraries (aka modules) are used to add extra functions. Use import, and redefine for brevity.\n",
    "```python\n",
    "import random as r\n",
    "import numpy as np```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x = 25\n",
    "y = np.sqrt(x)\n",
    "print (y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use command *from* library *import* * to import complete libraries, so no need to continuously reference (you can remove \"np.\" before \"sqrt\")  \n",
    "```python\n",
    "from numpy import *\n",
    "from random import *```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0\n"
     ]
    }
   ],
   "source": [
    "from numpy import *\n",
    "x = 25\n",
    "y = sqrt(x)\n",
    "print (y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use *randint* to return a random integer between (and including) comma values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "from random import *\n",
    "x = randint(1,10)\n",
    "print (x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Loops}}$\n",
    "\"For\" loops = repeat for certain amount of time\n",
    "\n",
    "\"While\" loops = repeat code while a condition is true."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "we managed to get out of the while loop after  1  loop(s)\n"
     ]
    }
   ],
   "source": [
    "x = 1\n",
    "y = 0\n",
    "while (x!=5):\n",
    "    x = randint(1,5)\n",
    "    print (x)\n",
    "    y = y+1\n",
    "print (\"we managed to get out of the while loop after \", str(y), \" loop(s)\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Example: Sphynx Test}}$\n",
    "You have encountered a wild sphynx. The sphynx has chosen a number between 1 and 20. \n",
    "\n",
    "You must guess the number to win. If you lose, you must keep guessing until you choose the correct number. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "Guess a number:   12\n",
      "YOU LOSE SUCKER, TRY AGAIN     13\n",
      "YOU LOSE SUCKER, TRY AGAIN     8\n",
      "YOU DIE... Just kidding, you win, the answer was 8\n"
     ]
    }
   ],
   "source": [
    "sphynx = randint(1,20)\n",
    "print(sphynx)\n",
    "guess = 0\n",
    "\n",
    "guess = int(input (\"Guess a number:   \"))\n",
    "\n",
    "while(sphynx!=guess):\n",
    "    guess = int(input (\"YOU LOSE SUCKER, TRY AGAIN     \"))\n",
    "\n",
    "print(\"YOU DIE... Just kidding, you win, the answer was\", guess)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-------------------------------------------------*Fin*-------------------------------------------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
