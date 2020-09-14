#include "palindrome.h"

/**
 * is_palindrome - function that checks whether or not a given unsigned
 * integer is a palindrome.
 * @n: Number to be checked
 * Return: 1 if n is a palindrome, and 0 otherwise
 */
int is_palindrome(unsigned long n) {
	if (_reverse_number(n, 0) == n)
		return (1);
	else
		return (0);
}


/**
 * _reverse_number - Recursive function that returns the reverse number.
 * @n: Number to Check
 * @temp: Store number
 * Return: Number reversed
 */
unsigned long _reverse_number(unsigned long n, unsigned long temp) {
	if (n == 0)
		return (temp);

	return (_reverse_number(n / 10, (temp * 10) + (n % 10)));
}
