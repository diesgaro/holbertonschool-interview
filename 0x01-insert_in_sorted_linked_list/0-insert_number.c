#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node into a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *last;

	current = *head;
	last = NULL;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current)
		{
			if (new->n < current->n)
			{
				if (last)
				{
					new->next = last->next;
					last->next = new;
				}
				else
				{
					new->next = current;
					*head = new;
				}
				break;
			}
			if (current->next == NULL)
			{
				current->next = new;
				break;
			}
			last = current;
			current = current->next;
		}
	}
	return (new);
}
