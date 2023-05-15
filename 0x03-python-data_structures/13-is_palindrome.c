#include "lists.h"
#include <stddef.h>

/**
 * @*reverse_listint - Reverses a linked list in palindome
 * @head: Pointer to a pointer pointing to the first item in the list
 * Return: The new head of the reversed list
 */

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

listint_t *reverse_listint(listint_t **head)
{
  listint_t *node = *head, *next, *prev = NULL;

  while (node)
    {
      next = node->next;
      node->next = prev;
      prev = node;
      node = next;
    }
  *head = prev;
  return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * reverse_listint - Reverses a linked list in place
 * @head: A pointer to the head of the linked list
 * Return: if not a palindrome - 0. If a palindrome - 1.
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *half;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;

	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;

	for (i = 0; i < (size / 2) - 1; i++)
	temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse_listint(&temp);
	half = rev;
	temp = *head;

	while (rev)
	{
	if (temp->n != rev->n)
		return (0);
	temp = temp->next;
	rev = rev->next;
	}
	reverse_listint(&half);
	return (1);
}
