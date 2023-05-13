#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>

/**
 * is_palindrome - checks id the reverse is equal to original
 * @head: pointer to linked list
 * Return: 1 if true and 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	}

	listint_t *slow = *head, *fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL, *curr = slow->next, *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	listint_t *p1 = *head, *p2 = prev;

	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		return (0);
	p1 = p1->next;
	p2 = p2->next;
	}
	curr = prev, prev = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	slow->next = prev;
	return (1);
}
