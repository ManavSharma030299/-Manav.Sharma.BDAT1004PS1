#!/usr/bin/env python
# coding: utf-8

# Question 1

# 1 What data type is each of the following?

# 
# | Variable     | Data type   
# | :------------ | -------------:|
# |5             |int.
# |5.0           | double.
# |5 > 1         | bool.
# |'5'           | char.
# |5 * 2         |int.
# |'5' * 2       |compiletime erro.
# |'5' + '2'     | compiletime error.
# |5 / 2         | double.
# |5 % 2         | int.
# |{5, 2, 1}     | int[].
# |5 == 3        | bool.
# |Pi            | not a built-in data type in C#, but you could represent the number Pi as a constant of type double.

# 2 Write (and evaluate) C# expressions that answer these questions:

# a. How many letters are there in 'Supercalifragilisticexpialidocious'?
# b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring?
# c. Which of the following words is the longest:
# Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or
# Bababadalgharaghtakamminarronnkonn?
# d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian',
# 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?
# 

# using System;
# 
# namespace ExpressionEvaluation
# {
#     class Program
#     {
#         static void Main(string[] args)
#         {
#             string word = "Supercalifragilisticexpialidocious";
#             int letterCount = 0;
#             bool containsIce = false;
#             for (int i = 0; i < word.Length - 2; i++) // creating loop where it will run for word max lenght
#             {
#                 if (word[i] == 'i' && word[i + 1] == 'c' && word[i + 2] == 'e') // checking until all needed condition are met for every itteration of i
#                 {
#                     containsIce = true;//change the value to true if condition are met
#                     break;
#                 }
#             }
#             letterCount = word.Length; //setting letter cout value to string length
# 
#             string[] words = new string[] {
#                 "Supercalifragilisticexpialidocious",
#                 "Honorificabilitudinitatibus",
#                 "Bababadalgharaghtakamminarronnkonn"
#             };
# 
#             string longestWord = words[0];
#             for (int i = 1; i < words.Length; i++)
#             {
#                 if (words[i].Length > longestWord.Length) // equating value of word and replacing it with max one
#                 {
#                     longestWord = words[i];
#                 }
#             }
# 
#             string[] composers = new string[] {
#                 "Berlioz",
#                 "Borodin",
#                 "Brian",
#                 "Bartok",
#                 "Bellini",
#                 "Buxtehude",
#                 "Bernstein"
#             };
# 
#             for (int i = 0; i < composers.Length; i++) //first loof for intial variable froom given array
#             {
#                 for (int j = i + 1; j < composers.Length; j++)// second loop for next variable from the array to comapre it 
#                 {
#                     if (String.Compare(composers[j], composers[i], StringComparison.OrdinalIgnoreCase) < 0)//usnig inbuilt function which check if integer value is greater beteen both
#                     {
#                         string temp = composers[i];//using temp variable to swap valuses if conditons are met
#                         composers[i] = composers[j];
#                         composers[j] = temp;
#                     }
#                 }
#             }
# 
#             Console.WriteLine("The number of letters in 'Supercalifragilisticexpialidocious' is " + letterCount);
#             Console.WriteLine("Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? " + containsIce);
#             Console.WriteLine("The longest word is: " + longestWord);
#             Console.WriteLine("The first composer in the dictionary is: " + composers[0]);
#             Console.WriteLine("The last composer in the dictionary is: " + composers[composers.Length - 1]);
#         }
#     }
# }

# ![2.png](attachment:2.png)

# Question 3 C#
# 

# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3
# sides of a triangle and returns the area of the triangle. By Heron's formula, the area
# of a triangle with side lengths a, b, and c is s(s − a)(s −b)(s −c), where
# s = (a + b + c)/2.
# >>> triangleArea(2,2,2)
# 1.7320508075688772

# namespace TriangleArea
# {
#     class Program
#     {
#         static void Main(string[] args)
#         {
#             Console.WriteLine("Enter the first side length: ");
#             double a = double.Parse(Console.ReadLine());
# 
#             Console.WriteLine("Enter the second side length: ");
#             double b = double.Parse(Console.ReadLine());
# 
#             Console.WriteLine("Enter the third side length: ");
#             double c = double.Parse(Console.ReadLine());
# 
#             Console.WriteLine("The area of the triangle is: " + TriangleArea(a, b, c));
#         }
# 
#         static double TriangleArea(double a, double b, double c)
#         {
#             double s = (a + b + c) / 2;
#             return Math.Sqrt(s * (s - a) * (s - b) * (s - c));// returns square root of the following equation
#         }
#     }
# }
# 

# ![3.png](attachment:3.png)

# Question 4 C#

# Write a program in C# Sharp to separate odd and even integers in separate arrays.
# Go to the editor
# Test Data :
# Input the number of elements to be stored in the array :5
# Input 5 elements in the array :
# element - 0 : 25
# element - 1 : 47
# element - 2 : 42
# element - 3 : 56
# element - 4 : 32 

#   class Program
#     {
#         static void Main(string[] args)
#         {
#             Console.Write("Enter the number of elements to be stored in the array: ");
#             int n = int.Parse(Console.ReadLine());//coverts to integer if if input is string
#             int[] arr = new int[n];// n number array
#             int[] evenArr = new int[n];// n number arry
#             int[] oddArr = new int[n];//n number array
# 
#             int evenIndex = 0;
#             int oddIndex = 0;
# 
#             Console.WriteLine("Enter " + n + " elements in the array: ");
#             for (int i = 0; i < n; i++)
#             {
#                 Console.Write("element - " + i + ": ");
#                 arr[i] = int.Parse(Console.ReadLine());//using main array while  converts to integer if needed
# 
#                 if (arr[i] % 2 == 0)//to check if ineterg is even
#                 {
#                     evenArr[evenIndex] = arr[i];
#                     evenIndex++;
#                 }
#                 else
#                 {
#                     oddArr[oddIndex] = arr[i];
#                     oddIndex++;
#                 }
#             }
# 
#             Console.WriteLine("Even Elements: ");
#             for (int i = 0; i < evenIndex; i++)
#             {
#                 Console.Write(evenArr[i] + " ");
#             }
# 
#             Console.WriteLine("\nOdd Elements: ");
#             for (int i = 0; i < oddIndex; i++)
#             {
#                 Console.Write(oddArr[i] + " ");
#             }
#         }
#     }
# }
# 

# ![4.png](attachment:4.png)

# Question 5 C#
# 

# a. Write a function inside(x,y,x1,y1,x2,y2) that returns True or False
# dependingonwhetherthepoint(x,y)liesintherectanglewithlowerleft
# corner (x1,y1) and upper right corner (x2,y2).
# >>> inside(1,1,0,0,2,3)
# True
# >>> inside(-1,-1,0,0,2,3)
# False
# b. Use function inside()from part a. to write an expression that tests whether
# the point (1,1) lies in both of the following rectangles: one with lower left
# corner (0.3, 0.5) and upper right corner (1.1, 0.7) and t

# namespace Rectangle
# {
#     class Program
#     {
# 
#         static bool inside(double x, double y, double x1, double y1, double x2, double y2)
#         {
#             return x >= x1 && x <= x2 && y >= y1 && y <= y2;
#         }
#         static void Main(string[] args)
#         {
#             // Test the function inside
#             Console.WriteLine(inside(1, 1, 0, 0, 2, 3));  
#             Console.WriteLine(inside(-1, -1, 0, 0, 2, 3));  
# 
#             // Test whether the point (1, 1) lies in both of the rectangles
#             Console.WriteLine(inside(1, 1, 0.3, 0.5, 1.1, 0.7) && inside(1, 1, 0.5, 0.2, 1.1, 2));
#         }
# 
#     }
# }

# ![5.png](attachment:5.png)

# Question 6 Python

# You can turn a word into pig-Latin using the following two rules(simplified):
# • If the word starts with a consonant, move that letter to the end and append
# 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# • If the word starts with a vowel, simply append 'way' to the end of the word.
# For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For
# our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# Write a function pig() that takes a word (i.e., a string) as input and returns its pigLatin form. Your function should still work if the input word contains upper case
# characters. Your output should always be lower case however.
# 

# In[3]:


def pig(word):
    word = word.lower()
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"

print(pig("happy"))
print(pig("Enter"))


# Question 7 Python

# File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic.
# Write a function bldcount() that reads the file with name name and reports (i.e.,
# prints) how many patients there are in each bloodtype.
# >>> bldcount('bloodtype.txt')
# There are 10 patients of blood type A.
# There is one patient of blood type B.
# There are 10 patients of blood type AB.
# There are 12 patients of blood type O.
# There are no patients of blood type OO.

# In[10]:


def bldcount(name):
    with open(name) as f:
        blood_types = f.read().splitlines()
    blood_counts = {}
    for blood_type in blood_types:
        if blood_type not in blood_counts:
            blood_counts[blood_type] = 1
        else:
            blood_counts[blood_type] += 1
    for blood_type, count in blood_counts.items():
        if count > 1:
            print("There are {} patients of blood type {}.".format(count, blood_type))
        else:
            print("There is one patient of blood type {}.".format(blood_type))

bldcount("bloodtype.txt")


# Question 8 Python

# Write a function curconv() that takes as input:
# 1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or
# 'EUR' for the Euro)
# 2. an amount
# and then converts and returns the amount in US dollars.
# 

# In[25]:


def curconv(currency, amount):
    exchange_rates = {}
    f = open("currencies.txt", "r")
    lines = f.readlines()
    for line in lines:
        elements = line.strip().split()
        code = elements[0]
        rate = float(elements[1])
        exchange_rates[code] = rate
    f.close()
    if currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {currency}")
    rate = exchange_rates[currency]
    return amount * rate
print(curconv('EUR', 100))
print(curconv('JPY', 100))


# Question 9 Python
# 

# Each of the following will cause an exception (an error). Identify what type of
# exception each will cause.

# Adding 6 + ‘a’ -
# TypeError
# 
# Referring to the 12th item of a list that has only 10 items -
# IndexError
# 
# Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0) - 
# ValueError
# 
# Using an undeclared variable, such as print(x) when x has not been defined - NameError
# 
# Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory -
# FileNotFoundError

# Question 10 Python

# Encryption is the process of hiding the meaning of a text by substituting letters in the
# message with other letters, according to some system. If the process is successful, no
# one but the intended recipient can understand the encrypted message. Cryptanalysis
# refers to attempts to undo the encryption, even if some details of the encryption are
# unknown (for example, if an encrypted message has been intercepted). The first step
# of cryptanalysis is often to build up a table of letter frequencies in the encrypted text.
# Assume that the string letters is already defined as
# 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies()
# that takes a string as its only parameter, and returns a list of integers, showing the
# number of times each character appears in the text. Your function may ignore any
# characters that are not in letters.
# 

# In[26]:


def frequencies(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    freq_list = [0] * 26
    for char in text:
        char = char.lower()
        if char in letters:
            index = letters.index(char)
            freq_list[index] += 1
    return freq_list

print(frequencies('The quick red fox got bored and went home.'))
print(frequencies('apple'))

