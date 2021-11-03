# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def prime(n):
        for i in range(1, n+1):
            if i > 1:
                for j in range(2, i):
                    if i%j == 0:
                        break
                else:
                    print(i)
prime(88)
