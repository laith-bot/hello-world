{
 "cells": [
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
      "-14 -5 -39 -5 -7 -1\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "x = list(map(int,input().split()))\n",
    "b = 0\n",
    "for i in x:\n",
    "    if i < 0:\n",
    "        b+=1\n",
    "print(b)\n",
    "    \n",
    "    \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
