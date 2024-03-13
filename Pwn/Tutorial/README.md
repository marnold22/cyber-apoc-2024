# Tutorial

## FLAG: HTB{gg_3z_th4nk5_f0r_th3_tut0r14l} 

## Status: Complete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Before we start, practice time!

## NOTES

1. Start Docker
   1. IP: 83.136.253.126
   2. PORT: 39779
2. Extract content
   1. > unzip pwn_tutorial.zip
      1. Readme.txt, test, test.c

        ```c
            #include <stdio.h>
            #include <limits.h>

            int add(int x, int y) { return x + y; }

            void main(){
                int n1, n2;
                printf("INT_MAX value: %d\n\nEnter 2 numbers: ", INT_MAX);
                scanf("%d %d", &n1, &n2);
                printf(n1 < 0 || n2 < 0 ? "\n[-] Negative values detected! Exiting..\n" : "\nThe sum of %d and %d is %d\n\n", n1, n2, add(n1, n2));
            }
        ```
3. Connect to Docker
   1. > nc 83.136.253.126 39779

        ```text
            This is a simple questionnaire to get started with the basics.
            ◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉
            ◉  INT_MAX = 2147483647                  (for 32-bit Integers)
            ◉  INT_MAX = 9,223,372,036,854,775,807   (for 64-bit Integers)
            ◉  INT_MIN = –2147483648                 (for 32-bit Integers)
            ◉  INT_MIN = –9,223,372,036,854,775,808  (for 64-bit Integers)
            ◉  When this limit is passed, C will proceed with an 'unusual' behavior. For example, if we
            ◉  add INT_MAX + 1, the result will NOT be 2147483648 as expected, but something else.
            ◉  The result will be a negative number and not just a random negative number, but INT_MIN.
            ◉  This 'odd' behavior, is called Integer Overflow.
            ◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉
        ```

      1. QUESTIONS
         1. "Is it possible to get a negative result when adding 2 positive numbers in C? (y/n)"
            1. Y
         2. "What's the MAX 32-bit Integer value in C?"
            1. 2147483647
         3. "What number would you get if you add INT_MAX and 1?"
            1. -2147483648
         4. "What number would you get if you add INT_MAX and INT_MAX?"
            1. -2
         5. "What's the name of this bug? (e.g. buffer overflow)"
            1. Integer Overflow
         6. What's the MIN 32-bit Integer value in C?
            1. -2147483648
         7. What's the number you can add to INT_MAX to get the number -2147482312?
            1. 1337
4. FLAG
   1. FLAG: `HTB{gg_3z_th4nk5_f0r_th3_tut0r14l} `