#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer with the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	else
		return (_palindrome(*head, _length(*head)));
}

/**
 * _length - Function to get the length of a linked list
 * @head: Pointer with the head of the linked list
 * Return: The length of the linked list
 */
int _length(listint_t *head)
{
	listint_t *current;
	int n;

	current = head;
	n = 0;

	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * _palindrome - Function that evaluate if the linked list  is palindrome
 * @node: Current node of linked list
 * @l: Current length of linked list
 * Return: 1 if string is palindrome or 0 if not
 */
int _palindrome(listint_t *node, int l)
{
	if (node->n == _get_value_last_node(node, l))
		if (l <= 0)
			return (1);
		else
			return (_palindrome(node->next, l - 2));
	else
		return (0);
}

/**
 * _get_value_last_node - Function that get the last value of linked list
 * @node: Current node of linked list
 * @l: Current length of linked list
 * Return: The value of n
 */
int _get_value_last_node(listint_t *node, int l)
{
	listint_t *current = node;
	int i;

	for (i = 1; i < l; i++)
	{
		current = current->next;
	}

	return (current->n);
}
