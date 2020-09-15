{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# $\\color{Green}{\\text{Practice Problems}}$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date and time last edit (Y-M-D): \n",
      "2019-03-13 16:24:13\n"
     ]
    }
   ],
   "source": [
    "from datetime import *\n",
    "now = datetime.now()\n",
    "print (\"Date and time last edit (Y-M-D): \")\n",
    "print (now.strftime (\"%Y-%m-%d %H:%M:%S\"))\n",
    "\t"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Questions}}$\n",
    "* Tab Indicator (Above)\n",
    "* Prime Numbers\n",
    "* Problem 18\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 34}}$\n",
    "**Project Euler #9**\n",
    "\n",
    "A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which $a^2 + b^2 = c^2$\n",
    "For example:\n",
    "```python \n",
    "3**2 + 4**2 = 9 + 16 = 25 = 5**2```\n",
    "\n",
    "There exists exactly one Pythagorean triplet for which $a + b + c = 1000$. Find the product abc."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 387,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "31875000\n"
     ]
    }
   ],
   "source": [
    "for c in range (3, 500):\n",
    "    for b in range (2, c):\n",
    "        for a in range (1, b):\n",
    "            if (a + b + c == 1000):\n",
    "                if (a**2 + b**2 == c**2):\n",
    "                    print (a*b*c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 33}}$\n",
    "**Project Euler #8**\n",
    "\n",
    "The four adjacent digits in the 1000-digit number that have the greatest product are $9 × 9 × 8 × 9 = 5832$\n",
    "\n",
    "73167176531330624919225119674426574742355349194934\n",
    "96983520312774506326239578318016984801869478851843\n",
    "85861560789112949495459501737958331952853208805511\n",
    "12540698747158523863050715693290963295227443043557\n",
    "66896648950445244523161731856403098711121722383113\n",
    "62229893423380308135336276614282806444486645238749\n",
    "30358907296290491560440772390713810515859307960866\n",
    "70172427121883998797908792274921901699720888093776\n",
    "65727333001053367881220235421809751254540594752243\n",
    "52584907711670556013604839586446706324415722155397\n",
    "53697817977846174064955149290862569321978468622482\n",
    "83972241375657056057490261407972968652414535100474\n",
    "82166370484403199890008895243450658541227588666881\n",
    "16427171479924442928230863465674813919123162824586\n",
    "17866458359124566529476545682848912883142607690042\n",
    "24219022671055626321111109370544217506941658960408\n",
    "07198403850962455444362981230987879927244284909188\n",
    "84580156166097919133875499200524063689912560717606\n",
    "05886116467109405077541002256983155200055935729725\n",
    "71636269561882670428252483600823257530420752963450\n",
    "\n",
    "Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 355,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23514624000\n"
     ]
    }
   ],
   "source": [
    "from numpy import *\n",
    "num = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)\n",
    "new = 0\n",
    "\n",
    "for x in range(len(num)):\n",
    "    digit_list = list(num[x:x+13])\n",
    "    digit_list = [int(i) for i in digit_list]\n",
    "    product = prod(digit_list)\n",
    "    for number in range (len(num)):\n",
    "        if product > new:\n",
    "            new = product\n",
    "print (new)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 32}}$\n",
    "**Project Euler #7**\n",
    "\n",
    "By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.\n",
    "\n",
    "What is the $10001st$ prime number?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "primelist = [2]\n",
    "\n",
    "def prime(n):\n",
    "    if (n<2):\n",
    "        return False\n",
    "    for i in range (2, n//2+1):\n",
    "        if (n % i == 0):\n",
    "            return False\n",
    "    return True\n",
    "    \n",
    "for num in range (1, 200000, 2):\n",
    "    if prime(num):\n",
    "        primelist.append(num)\n",
    "\n",
    "print (primelist[10000:10001])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 31}}$\n",
    "**Project Euler #6**\n",
    "\n",
    "The sum of the squares of the first ten natural numbers is $1^2 + 2^2 + ... + 10^2 = 385$. The square of the sum of the first ten natural numbers is\n",
    "$(1 + 2 + ... + 10)^2 = 552 = 3025$. Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 − 385 = 2640$\n",
    "\n",
    "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 370,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25502500 - 338350 = 25164150\n"
     ]
    }
   ],
   "source": [
    "hundred = list(range(101))\n",
    "squares = []\n",
    "\n",
    "for i in hundred:\n",
    "    square = i**2\n",
    "    squares.append(square)\n",
    "\n",
    "large = sum(hundred)**2    \n",
    "small = sum(squares)\n",
    "print (large, \"-\", small, \"=\", large-small)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 30}}$\n",
    "**Project Euler #5**\n",
    "\n",
    "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\n",
    "\n",
    "What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "232792560\n"
     ]
    }
   ],
   "source": [
    "#Dan Edit \n",
    "numbers = list(range(11, 21))\n",
    "\n",
    "for n in range (0, 99999999999, 2520):\n",
    "    divide = [x for x in range (11, 21) if n % x == 0]\n",
    "    if divide == numbers:\n",
    "        if n > 0:\n",
    "            break\n",
    "            \n",
    "print (n)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 29}}$\n",
    "\n",
    "**Project Euler #4**\n",
    "\n",
    "A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is $9009 = 91 × 99$\n",
    "\n",
    "Find the largest palindrome made from the product of two 3-digit numbers."
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
      "906609 is the largest palindromic number made from the product of three-digit numbers, and those numbers are 913 and 993\n"
     ]
    }
   ],
   "source": [
    "#Dan Edit\n",
    "palindrome = 0\n",
    "\n",
    "for x in range (100,1000):\n",
    "    for y in range (100,1000):\n",
    "        num = str(x*y)\n",
    "        rev = num[::-1]\n",
    "        if num == rev and int(num) > palindrome: \n",
    "            palindrome = int(num)\n",
    "            number_one = x\n",
    "            number_two = y\n",
    "print (palindrome, \"is the largest palindromic number made from the product of three-digit numbers, and those numbers are\", number_one, \"and\", number_two)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 28}}$\n",
    "\n",
    "**Prac #16**\n",
    "\n",
    "Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.\n",
    "\n",
    "Extra:\n",
    "* Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."
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
      "How strong do you want your password to be?\n",
      "Please choose: Weak, Medium, or Strong   strong\n",
      "How many characters do you want your password to be? [1-20]:  16\n",
      "mQkeuFhztDiWsY?x\n"
     ]
    }
   ],
   "source": [
    "from random import *\n",
    "word = [\"beaver\", \"quail\", \"dolphin\", \"tiger\", \"tapir\", \"lynx\", \"armadillo\", \"salamander\", \"ferret\", \"herring\", \"sloth\", \"hippopotamus\", \"pengiun\"]\n",
    "sym = [\"!\", \"*\", \"?\", \"@\", \"&\", \"%\", \"$\", \"#\"]\n",
    "num = \"012345689\"\n",
    "all = \"abcdefghijklmnopqrstuvqxyz012345689ABCDEFGHIJKLMNOPQRSTUVWXYZ!?*$%@#$\"\n",
    "\n",
    "       \n",
    "while True: \n",
    "    x = input(\"How strong do you want your password to be?\" + \"\\n\" + \"Please choose: Weak, Medium, or Strong   \").upper()\n",
    "    rand_word = choice(word)\n",
    "    rand_sym = choice(sym)\n",
    "    if x == \"WEAK\":\n",
    "        print (rand_word, randint(1,9), sep=\"\")\n",
    "        break\n",
    "    elif x == \"MEDIUM\":\n",
    "        medium = (rand_word) + (rand_sym) + \"\".join(sample(num,2))\n",
    "        print (medium)\n",
    "        break\n",
    "    elif x == \"STRONG\":\n",
    "        length = int(input(\"How many characters do you want your password to be? [1-20]:  \")) \n",
    "        strong = \"\".join(sample(all,length))\n",
    "        print (strong)\n",
    "        break\n",
    "    else:\n",
    "        print (\"Please choose either Weak, Medium, or Strong\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 27}}$\n",
    "\n",
    "**Prac #15**\n",
    "\n",
    "Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a sentence:   Hello it is me\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'me is it Hello'"
      ]
     },
     "execution_count": 196,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = input (\"Please enter a sentence:   \")\n",
    "def stringy(x):\n",
    "    return \" \".join(x.split()[::-1])\n",
    "\n",
    "stringy(x)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 26}}$\n",
    "\n",
    "**Prac #14**\n",
    "\n",
    "Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.\n",
    "\n",
    "Extras:\n",
    "\n",
    "* Write two different functions to do this - one using a loop and constructing a list, and another using sets.\n",
    "* Go back and do Exercise 5 using sets, and write the solution for that in a different function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 4, 4, 8, 8, 9, 9]\n",
      "[1, 2, 3, 4, 8, 9]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "([1, 2, 3, 4, 8, 9], [1, 2, 3, 4, 8, 9])"
      ]
     },
     "execution_count": 184,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from numpy import *\n",
    "l = random.choice (10, 10, replace = True)\n",
    "l.sort()\n",
    "print(list(l))\n",
    "\n",
    "# With function and loop\n",
    "def l_loop(x):\n",
    "    y = []\n",
    "    for num in x:\n",
    "        if num not in y:\n",
    "            y.append(num)\n",
    "    return y\n",
    "\n",
    "# With function and set\n",
    "def l_set(x):\n",
    "    return list(set(x))\n",
    "\n",
    "# With just set \n",
    "print (list(set(l)))\n",
    "\n",
    "# Results\n",
    "(l_loop(l), l_set(l))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 25}}$\n",
    "\n",
    "**Prac #13**\n",
    "\n",
    "Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many Fibonacci numbers would you like to generate?  6\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[1, 1, 2, 3, 5, 8]"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def fib():\n",
    "    count = int(input(\"How many Fibonacci numbers would you like to generate?  \"))\n",
    "    i = 1\n",
    "    if count == 0:\n",
    "        fib = []\n",
    "    elif count == 1:\n",
    "        fib = [1]\n",
    "    elif count == 2:\n",
    "        fib = [1, 1]\n",
    "    elif count > 2:\n",
    "        fib = [1, 1]\n",
    "        while i < (count - 1):\n",
    "            fib.append(fib[i]+fib[i-1])\n",
    "            i += 1\n",
    "    return fib\n",
    "fib()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 24}}$\n",
    "\n",
    "**Prac #12**\n",
    "\n",
    "Write a program that takes a list of numbers (for example, $a = [5, 10, 15, 20, 25]$ ) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[56, 36, 45, 68, 31]\n",
      "56 31\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[56, 31]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Standard\n",
    "from random import *\n",
    "a = sample(range(1,100), 5)\n",
    "\n",
    "print (a)\n",
    "print (a[0],a[len(a)-1])\n",
    "\n",
    "\n",
    "# Inside function\n",
    "def listy(a):\n",
    "    return [a[0], a[len(a)-1]]\n",
    "\n",
    "listy(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 23}}$\n",
    "\n",
    "**Prac #11**\n",
    "\n",
    "Ask the user for a number and determine whether the number is prime or not. A prime number has only two divisors; 1 and itself. Thus 1 is not a prime number but 2, 3, 5, etc. are."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number:   \n",
      "123456789\n",
      "123456789 is not a prime number.\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Please enter a number:   \" + \"\\n\"))\n",
    "\n",
    "if number <= 0 or number == 1:\n",
    "    prime = False\n",
    "elif number == 2:\n",
    "    prime = True\n",
    "else:\n",
    "    prime = True\n",
    "    for x in range (2, number - 1):\n",
    "        if number % x == 0:\n",
    "            prime = False\n",
    "            break\n",
    "\n",
    "if prime == True:\n",
    "    add = \"is\"\n",
    "else:\n",
    "    add = \"is not\"\n",
    "\n",
    "print (number, add, \"a prime number.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 22}}$\n",
    "\n",
    "**Prac #9**\n",
    "\n",
    "Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)\n",
    "\n",
    "Extras:\n",
    "\n",
    "* Keep the game going until the user types “exit”\n",
    "* Keep track of how many guesses the user has taken, and when the game ends, print this out.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type 'exit' in the input box any time to quit the game\n",
      "\n",
      "Please guess an integer between or inclusive of 1 and 9:   5\n",
      "\n",
      "Too low...    \n",
      "Guess again   8\n",
      "Great guess... you win! You guessed 2 times. Want to play again?\n",
      "Guess again   2\n",
      "\n",
      "Too low...    \n",
      "Guess again   7\n",
      "\n",
      "Too high...   \n",
      "Guess again   5\n",
      "Great guess... you win! You guessed 3 times. Want to play again?\n",
      "Guess again   exit\n",
      "\n",
      "Sad to see you leave!\n",
      "You played 2 times. You guessed 5 times in total.\n"
     ]
    }
   ],
   "source": [
    "from random import *\n",
    "num = randint(1,9)\n",
    "print (\"Type 'exit' in the input box any time to quit the game\" + \"\\n\")\n",
    "guess = input(\"Please guess an integer between or inclusive of 1 and 9:   \")\n",
    "count_total, count_guess, count_loop = 0, 0, 0\n",
    "\n",
    "while True:\n",
    "    if guess == \"exit\":\n",
    "        print (\"\\n\" + \"Sad to see you leave!\")\n",
    "        break\n",
    "    try:\n",
    "        guessINT = int(guess)\n",
    "        if guessINT < num:\n",
    "            print (\"\\n\" + \"Too low...    \")\n",
    "            count_guess = count_guess + 1\n",
    "        if guessINT > num:\n",
    "            print (\"\\n\" + \"Too high...   \")\n",
    "            count_guess = count_guess + 1\n",
    "        if guessINT == num:\n",
    "            count_guess = count_guess + 1\n",
    "            print (\"Great guess... you win! You guessed\", count_guess, \"times. Want to play again?\")\n",
    "            num = randint (1,9)\n",
    "            count_loop = count_loop + 1\n",
    "            count_guess = 0\n",
    "\n",
    "    except ValueError:\n",
    "        print (\"\\n\" + \"That's not an integer... try again! Type 'exit' any time to quit   \")\n",
    "    guess = input(\"Guess again   \")\n",
    "    count_total = count_total + 1\n",
    "\n",
    "print (\"You played\", count_loop, \"times. You guessed\", count_total, \"times in total.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 23}}$\n",
    "\n",
    "**Prac #8**\n",
    "\n",
    "Make a two-player Rock-Paper-Scissors game. Make sure to acknowledge the winner, and ask if the players would like to restart the game. Account for any inputs that are not rock, paper, or scissors. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Player 1: Please choose rock, paper, or scissors: rock\n",
      "\n",
      "You chose ROCK\n",
      "\n",
      "Player 2: Please choose rock, paper, or scissors: paper\n",
      "\n",
      "You chose PAPER\n",
      "\n",
      "Player 2 wins!!!\n",
      "\n",
      "Would you like to play again? Y or N:      y\n",
      "\n",
      "Player 1: Please choose rock, paper, or scissors: rock\n",
      "\n",
      "You chose ROCK\n",
      "\n",
      "Player 2: Please choose rock, paper, or scissors: paper\n",
      "\n",
      "You chose PAPER\n",
      "\n",
      "Player 2 wins!!!\n",
      "\n",
      "Would you like to play again? Y or N:      n\n",
      "\n",
      "Thanks for playing!\n"
     ]
    }
   ],
   "source": [
    "again = \"\"\n",
    "while 1 == 1:\n",
    "    if again == \"EXIT\":\n",
    "        break\n",
    "    else:\n",
    "        while True:\n",
    "            choice1 = input(\"\\n\" + \"Player 1: Please choose rock, paper, or scissors: \").upper()\n",
    "            if choice1 == \"ROCK\" or choice1 == \"PAPER\" or choice1 == \"SCISSORS\":\n",
    "                print ()\n",
    "                print (\"You chose \" + choice1)\n",
    "                break\n",
    "            else:\n",
    "                print ()\n",
    "\n",
    "        while True:\n",
    "            choice2 = input(\"\\n\" + \"Player 2: Please choose rock, paper, or scissors: \").upper()\n",
    "            if choice2 == \"ROCK\" or choice2 == \"PAPER\" or choice2 == \"SCISSORS\":\n",
    "                print ()\n",
    "                print (\"You chose \" + choice2)\n",
    "                break\n",
    "            else:\n",
    "                print ()\n",
    "\n",
    "        if choice1 == choice2:\n",
    "            print (\"It's a tie!\" + \"\\n\")\n",
    "        elif choice1 == \"ROCK\" and choice2 == \"SCISSORS\":\n",
    "            print (\"\\n\" + \"Player 1 wins!!!\" + \"\\n\")\n",
    "        elif choice1 == \"SCISSORS\" and choice2 == \"PAPER\":\n",
    "            print (\"\\n\" + \"Player 1 wins!!!\")\n",
    "        elif choice1 == \"PAPER\" and choice2 == \"ROCK\":\n",
    "            print (\"\\n\" + \"Player 1 wins!!!\" + \"\\n\") \n",
    "        else:\n",
    "            print (\"\\n\" + \"Player 2 wins!!!\" + \"\\n\")\n",
    "        again = input(\"Would you like to play again? Y or N:      \" ).upper()\n",
    "        if again == \"N\":\n",
    "            print (\"\\n\" + \"Thanks for playing!\")\n",
    "            break"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 22}}$\n",
    "\n",
    "**Prac #6**\n",
    "\n",
    "Ask the user for a string and print out whether this string is a palindrome or not."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a word here:  palindrome\n",
      "Your word is PALINDROME, and its reverse is EMORDNILAP\n",
      "This is not a palindrome \n"
     ]
    }
   ],
   "source": [
    "word = input(\"Please enter a word here:  \").upper()\n",
    "reverse = word[::-1]\n",
    "print (\"Your word is \" + word + \", and its reverse is \" + reverse)\n",
    "\n",
    "if (reverse == word):\n",
    "    print (\"This is a palindrome \")\n",
    "else:\n",
    "    print (\"This is not a palindrome \")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 21}}$\n",
    "\n",
    "**Prac #5**\n",
    "\n",
    "Take two lists, say for example these two:\n",
    "\n",
    " $ a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]$\n",
    " \n",
    " $ b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]$\n",
    "\n",
    "and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Randomly generate two lists to test this."
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
      "[26, 24, 12, 27, 13, 18, 17, 7, 29, 20, 5, 25]\n",
      "[20, 8, 1, 19, 22, 6, 4, 2, 29, 17, 12, 25, 21, 15, 23, 28]\n",
      "[12, 17, 20, 25, 29]\n"
     ]
    }
   ],
   "source": [
    "from random import *\n",
    "a = sample (range(1,30), 12)\n",
    "b = sample (range(1,30), 16)\n",
    "print (a)\n",
    "print (b)\n",
    "result = [x for x in set(a) if x in set(b)]\n",
    "print (result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 20}}$\n",
    "\n",
    "**Prac #4**\n",
    "\n",
    "Create a program that asks the user for a number and then prints out a list of all the divisors of that number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please choose a number to divide: 25\n",
      "[1, 5, 25]\n"
     ]
    }
   ],
   "source": [
    "listy = []\n",
    "number = int(input(\"Please choose a number to divide: \"))\n",
    "for y in range (1, number+1):\n",
    "    if (int(number) % y == 0):\n",
    "        listy.append(y)\n",
    "print (listy)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 19}}$\n",
    "\n",
    "**Prac #3**\n",
    "\n",
    "Take a list, for example:\n",
    "$a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]$ \n",
    "and write a program that prints out all the elements of the list that are less than 5.\n",
    "\n",
    "Extras:\n",
    "* Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.\n",
    "* Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number:  13\n",
      "[1, 1, 2, 3, 5, 8]\n"
     ]
    }
   ],
   "source": [
    "list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]\n",
    "list_b = []\n",
    "\n",
    "maximum = int(input(\"Please enter a number:  \"))\n",
    "for num in list_a:\n",
    "    if num < int(maximum):\n",
    "        list_b.append(num)\n",
    "print (list_b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 18}}$\n",
    "\n",
    "**Bat #2 (array123)**\n",
    "\n",
    "Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 476,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 476,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def array(x):\n",
    "    for i in range (len(x)):\n",
    "        if x[i] == 3 and x[i-1] == 2 and x[i-2] == 1:\n",
    "            return True\n",
    "    return False\n",
    "    \n",
    "array([1, 2, 1, 2, 3, 3, 4, 5,])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 473,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2520\n",
      "232792560\n"
     ]
    }
   ],
   "source": [
    "# This is the answer on the internet, I do not get it \n",
    "def smallest(n):\n",
    "    for x in range(n, factorial(n) + 1, n):\n",
    "        if yes(x, n):\n",
    "            return x\n",
    "    return no\n",
    "\n",
    "def yes(y, n):\n",
    "    for x in range(1, n):\n",
    "        if y % x != 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "def factorial(n):\n",
    "    if n > 1: return n * factorial(n - 1)\n",
    "    elif n >= 0: return 1\n",
    "    else: return no\n",
    "\n",
    "print (smallest(10)) \n",
    "print (smallest(20))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 17}}$\n",
    "\n",
    "**Project Euler #3**\n",
    "\n",
    "The prime factors of 13195 are 5, 7, 13 and 29.\n",
    "\n",
    "What is the largest prime factor of an input?\n",
    "What is the largest prime factor of the number 600851475143 ?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please choose an input:  29389832\n",
      "2\n",
      "127\n",
      "28927\n",
      "The largest prime factor of 29389832 is 28927\n"
     ]
    }
   ],
   "source": [
    "from sympy import *\n",
    "\n",
    "x = int(input (\"Please choose an input:  \"))\n",
    "\n",
    "for y in range (1, x + 1):\n",
    "    if x % y == 0 and isprime(y):\n",
    "        print (y)\n",
    "        factors = y\n",
    "        \n",
    "print(\"The largest prime factor of\", x, \"is\", factors)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 16}}$\n",
    "\n",
    "**Project Euler #2**\n",
    "\n",
    "Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:\n",
    "\n",
    "1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\n",
    "\n",
    "By considering the terms in the Fibonacci sequence whose values do not exceed an input limit, find the sum of the even-valued terms."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "limit = int(input (\"Please choose a limit:  \"))\n",
    "\n",
    "x, y, evens = 0, 1, 0 \n",
    "\n",
    "while x < limit:\n",
    "    print (x)\n",
    "    z = x + y\n",
    "    x = y\n",
    "    y = z\n",
    "    \n",
    "    if z % 2 == 0:\n",
    "        evens +=z;\n",
    "    \n",
    "print (\"The sum of the even numbers in this sequence is:\", evens)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 15}}$\n",
    "\n",
    "**Bat #2 (last2)**\n",
    "\n",
    "Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so \"hixxxhi\" yields 2 (including the end substring). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 471,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 471,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def last2(var):\n",
    "    if len(var) < 2:\n",
    "        return 0\n",
    "\n",
    "    last2 = var[len(var)-2:]\n",
    "    count = 0\n",
    "  \n",
    "    for x in range(len(var)):\n",
    "        sub = var[x:x+2]\n",
    "        if sub == last2:\n",
    "            count = count + 1\n",
    "\n",
    "    return count\n",
    "\n",
    "last2('hixxxxxhi'), last2('axxaxxaxx')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 14}}$\n",
    "\n",
    "**Bat #2 (string splosion)**\n",
    "\n",
    "Given a non-empty string like \"Code\" return a string like \"CCoCodCode\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('CCoCodCode', 'aababc')"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def string(str):\n",
    "    result = \"\"\n",
    "    for x in range(len(str)):\n",
    "        result = result + str[:x+1]     \n",
    "    return result\n",
    "\n",
    "string(\"Code\"), string ('abc')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 13}}$\n",
    "\n",
    "**Bat #2 (string bits)**\n",
    "\n",
    "Given a string, return a new string made of every other char starting with the first, so \"Hello\" yields \"Hlo\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def string(str):\n",
    "    result = \"\"\n",
    "    for x in range (len(str)):\n",
    "        if x % 2 == 0:\n",
    "            result = result + str[x]\n",
    "    return result\n",
    "\n",
    "string(\"abcdefghijk\"), string ('aabbccddeeffgg')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 12}}$\n",
    "\n",
    "**Bat #2 (count9)**\n",
    "\n",
    "Given an array of integers, return the number of 9's in the array."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def array_count(ninenine):\n",
    "  count = 0\n",
    "  for x in ninenine:\n",
    "    if x == 9:\n",
    "      count = count + 1\n",
    "\n",
    "  return count\n",
    "\n",
    "array_count([1, 5, 2, 0, 9, 6, 4, 9, 2, 7, 6, 9])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 11}}$\n",
    "\n",
    "**Bat #1 (sum double)**\n",
    "\n",
    "Given two int values, return their sum. Unless the two values are the same, then return double their sum."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 16)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def sum_double(x, y):\n",
    "  if x == y:\n",
    "    return 2*(x+y)\n",
    "  else:\n",
    "      return x + y\n",
    "sum_double (0,1), sum_double (4,4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 10}}$\n",
    "\n",
    "**Bat #1 (monkey trouble)**\n",
    "\n",
    "We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(True, False)"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def monkey_trouble(a_smile, b_smile):\n",
    "    if a_smile and b_smile:\n",
    "        return True\n",
    "    elif a_smile or b_smile: \n",
    "        return False \n",
    "    else:\n",
    "        return True\n",
    "    \n",
    "monkey_trouble(True, True), monkey_trouble(False, True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 9}}$\n",
    "\n",
    "**Bat #1 (sleep in)**\n",
    "\n",
    "The parameter weekday is \"True\" if it is a weekday, and the parameter vacation is \"True\" if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return \"True\" if we sleep in."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# With pre-defined\n",
    "def sleep_in(weekday, vacation):\n",
    "    if not weekday or vacation:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "sleep_in(True, False), sleep_in(True, False)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Are you on vacation?      N\n",
      "Is it a weekday? Y / N     Y\n",
      "\n",
      "No sleeping in today\n"
     ]
    }
   ],
   "source": [
    "# With inputs\n",
    "while True:\n",
    "    vacation = input (\"Are you on vacation?      \").upper()\n",
    "    if (vacation == \"Y\" or vacation == \"N\"):\n",
    "        break\n",
    "    else:\n",
    "        print (\"\\n\" + \"Please choose Y or N\" + \"\\n\")\n",
    "        \n",
    "while True:\n",
    "    weekday = input(\"Is it a weekday? Y / N     \").upper()\n",
    "    if (weekday == \"Y\" or weekday == \"N\"):\n",
    "        break\n",
    "    else:\n",
    "        print (\"\\n\" + \"Please choose Y or N\" + \"\\n\")\n",
    "\n",
    "        \n",
    "if (vacation == \"Y\" or weekday == \"N\"):\n",
    "    print (\"\\n\" + \"You get to sleep in today\")\n",
    "    \n",
    "else:\n",
    "    print (\"\\n\" + \"No sleeping in today\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 8}}$\n",
    "Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,\n",
    "between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line."
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
      "2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199\n"
     ]
    }
   ],
   "source": [
    "l = []\n",
    "for x in range  (2000, 3201):\n",
    "    if (x % 7 == 0) and (x % 5 != 0):\n",
    "        l.append(str(x))\n",
    "        \n",
    "print (', '.join(l))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 7}}$\n",
    "**Mosh #7**\n",
    "\n",
    "Write a function that prints all the prime numbers between 0 and limit where limit is a parameter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 470,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please choose a positive integer:  100\n",
      "2\n",
      "3\n",
      "5\n",
      "7\n",
      "11\n",
      "13\n",
      "17\n",
      "19\n",
      "23\n",
      "29\n",
      "31\n",
      "37\n",
      "41\n",
      "43\n",
      "47\n",
      "53\n",
      "59\n",
      "61\n",
      "67\n",
      "71\n",
      "73\n",
      "79\n",
      "83\n",
      "89\n",
      "97\n"
     ]
    }
   ],
   "source": [
    "# NOTE: Should work this out long-hand\n",
    "\n",
    "from sympy import *\n",
    "x = int(input (\"Please choose a positive integer:  \"))\n",
    "\n",
    "for y in range (0, x+1):\n",
    "    if isprime(y):\n",
    "        print (y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 6}}$\n",
    "**Mosh #6**\n",
    "\n",
    "Write a function of increasing *s. If rows is 5, it should print the following:\n",
    "    \n",
    "    *\n",
    "    * *\n",
    "    * * *\n",
    "    * * * *\n",
    "    * * * * *"
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
      "Please choose a positive integer:  5\n",
      "\n",
      " *\n",
      " * *\n",
      " * * *\n",
      " * * * *\n",
      " * * * * *\n"
     ]
    }
   ],
   "source": [
    "x = int(input (\"Please choose a positive integer:  \"))\n",
    "\n",
    "for y in range (0, x+1):\n",
    "    print (y*\" *\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 5}}$\n",
    "**Euler #1, Mosh #5**\n",
    "\n",
    "Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). \n"
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
      "Function will identify multiples of 3 and 5 below your limit.\n",
      "Please choose a postitive integer:          7\n",
      "\n",
      "0\n",
      "3\n",
      "5\n",
      "6\n",
      "\n",
      "The sum of the numbers in this list is 14\n"
     ]
    }
   ],
   "source": [
    "print (\"Function will identify multiples of 3 and 5 below your limit.\")\n",
    "\n",
    "x = int(input(\"Please choose a postitive integer:          \"))\n",
    "print ()\n",
    "\n",
    "for y in range (0, x+1):\n",
    "    if y % 3 == 0 or y % 5 == 0:\n",
    "        print (y)\n",
    "        numbers = 0\n",
    "\n",
    "print ()\n",
    "print (\"The sum of the numbers in this list is\",(y+y))        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 4}}$\n",
    "**Mosh #4**\n",
    "\n",
    "Write a function that takes a parameter called *limit*. It should print all the numbers between 0 and *limit* with a label to identify the even and odd numbers. For example, if the *limit* is 3, it should print:\n",
    "* 0 EVEN\n",
    "* 1 ODD\n",
    "* 2 EVEN\n",
    "* 3 ODD\n",
    "\n",
    "Bonus points to line up the words, and for sassy remarks regarding non-integer values. "
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
      "Please enter a integer between or including 0 and 100:   9\n",
      "\n",
      "0  EVEN\n",
      "1  ODD\n",
      "2  EVEN\n",
      "3  ODD\n",
      "4  EVEN\n",
      "5  ODD\n",
      "6  EVEN\n",
      "7  ODD\n",
      "8  EVEN\n",
      "9  ODD\n"
     ]
    }
   ],
   "source": [
    "x = (input(\"Please enter a integer between or including 0 and 100:   \"))\n",
    "print ()\n",
    "    \n",
    "if x.isdigit():\n",
    "    if type(x) == float: \n",
    "        print (\"Woah there... tried to trick me. FAIL.\")\n",
    "        x = int(input(\"Please pick an INTEGER: \"))\n",
    "    \n",
    "    else:\n",
    "        x = int(x)\n",
    "        if x > 100: \n",
    "            x = int(input(\"Please choose an integer LESS than 100: \"))\n",
    "\n",
    "        if x == 100:\n",
    "            for y in range (0, 10):\n",
    "                if y % 2 == 0:\n",
    "                    print (y, \"   EVEN\")\n",
    "                if y % 2 != 0:\n",
    "                    print (y, \"   ODD\")\n",
    "            for y in range (10, 100):\n",
    "                if y % 2 == 0: \n",
    "                    print (y, \"  EVEN\")\n",
    "                if y % 2 != 0: \n",
    "                    print (y, \"  ODD\")\n",
    "            for y in range (100, 101):\n",
    "                    print (y, \" EVEN\")\n",
    "\n",
    "        elif x <= 9:\n",
    "            for y in range (0, x+1):\n",
    "                if y % 2 == 0: \n",
    "                    print (y, \" EVEN\")\n",
    "                if y % 2 != 0: \n",
    "                    print (y, \" ODD\")\n",
    "\n",
    "        elif x > 9:\n",
    "            for y in range (0, 10):\n",
    "                if y % 2 == 0: \n",
    "                    print (y, \"  EVEN\")\n",
    "                if y % 2 != 0: \n",
    "                    print (y, \"  ODD\")\n",
    "            for y in range (10, x+1):\n",
    "                if y % 2 == 0: \n",
    "                    print (y, \" EVEN\")\n",
    "                if y % 2 != 0: \n",
    "                    print (y, \" ODD\")\n",
    "    \n",
    "else:\n",
    "    try:\n",
    "        val = int(x)\n",
    "        if (val < 0):\n",
    "            x = (input(\"Please choose a POSITIVE integer:   \"))\n",
    "        else:\n",
    "            print (\"XXX\")\n",
    "    except ValueError:\n",
    "        print (\"Sneaky bastard...\")\n",
    "        print ()\n",
    "        x = (input(\"Please choose an INTEGER:   \"))\n",
    "        print ()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 3}}$\n",
    "**Mosh #3**\n",
    "\n",
    "Write a function for checking the speed of drivers. This function should have one parameter: speed\n",
    "* If speed less than 70, it should print \"Ok\"\n",
    "* Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total demerit points\n",
    "* If the driver gets more than 12 points, the function should print \"License suspended\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter the driver's name:   Anu\n",
      "\n",
      "What is Anu's gender? Male, female, or nonbinary (M/F/N):   M\n",
      "\n",
      "Enter Anu's speed:   32\n",
      "\n",
      "Speed up there Grandpa!\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Please enter the driver's name:   \")\n",
    "print ()\n",
    "gender = input(\"What is \" + name + \"'s gender? Male, female, or nonbinary (M/F/N):   \").upper()\n",
    "print ()\n",
    "\n",
    "if gender != \"M\" and gender != \"F\" and gender != \"N\":\n",
    "    gender = input(\"Please enter either M, F, or N\")\n",
    "\n",
    "n = int(input (\"Enter \" + name + \"'s speed:   \"))\n",
    "print ()\n",
    "\n",
    "    \n",
    "if n <= 40 and gender == \"M\":\n",
    "    print (\"Speed up there Grandpa!\")\n",
    "    \n",
    "if n <= 40 and gender == \"F\":\n",
    "    print (\"Speed up there Grandma!\")\n",
    "\n",
    "if n <= 40 and gender == \"N\":\n",
    "    print (\"Speed up there Grandparent!\")\n",
    "    \n",
    "if n <= 55 and n > 40:\n",
    "    print (name + \" should probably speed up a bit...\")\n",
    "    \n",
    "if n <= 70 and n > 55:\n",
    "    print (name + \" is not speeding. Yay for \" + name + \"!\")\n",
    "\n",
    "if n > 70:\n",
    "    print (name + \" has exceeded the speed limit by\", n-70, \"km/hr\")\n",
    "\n",
    "elif n == 75:\n",
    "    print (\"Demerit Point = 1\")\n",
    "\n",
    "if int((n-70)/5) >= 12:\n",
    "    print (\"License suspended... You could have killed someone!\")\n",
    "    \n",
    "if n > 75 and n % 5 == 0:\n",
    "    print ()\n",
    "    print (\"Demerit Points = \", int((n-70)/5))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 2}}$\n",
    "**Mosh #2**\n",
    "\n",
    "Write a function called fizz_buzz that takes a number:\n",
    "* If the number is divisible by 3, it should return \"Fizz\"\n",
    "* If the number is divisible by 5, it should return \"Buzz\"\n",
    "* If the number is divisible by both 3 and 5, it should return \"FizzBuzz\"\n",
    "* If the number if not divisible by either 3 or 5, it should return \"BuzzFizz\""
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
      "Pick a number   15\n",
      "FizzBuzz\n"
     ]
    }
   ],
   "source": [
    "n = int(input (\"Pick a number   \"))\n",
    "\n",
    "if n % 3 == 0 and n % 5 ==0:\n",
    "    print (\"FizzBuzz\")\n",
    "    \n",
    "elif n % 3 == 0:\n",
    "    print (\"Fizz\")\n",
    "    \n",
    "elif n % 5 == 0:\n",
    "    print (\"Buzz\")\n",
    "    \n",
    "else:\n",
    "    print (\"BuzzFizz\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Problem 1}}$\n",
    "**Mosh #1**\n",
    "\n",
    "Write a function that returns the greater of two numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pick a number   4\n",
      "Now pick another number   6\n",
      "The larger of the two numbers is 6\n"
     ]
    }
   ],
   "source": [
    "x, y = int(input (\"Pick a number   \")), int(input (\"Now pick another number   \"))\n",
    "\n",
    "if x > y:\n",
    "    print (\"The larger of the two numbers is\", x)\n",
    "elif x == y:\n",
    "    print (\"The numbers are equal\")\n",
    "else:\n",
    "    print (\"The larger of the two numbers is\", y) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## $\\color{blue}{\\text{Sources}}$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* [Programming With Mosh](https://programmingwithmosh.com/python/python-exercises-and-questions-for-beginners/) (Mosh)\n",
    "* [Coding Bat](https://codingbat.com/python) (Bat)\n",
    "* [Practice Python](http://www.practicepython.org/exercises/) (Prac)\n",
    "* [Project Euler](https://projecteuler.net/archives) (Euler)"
   ]
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
