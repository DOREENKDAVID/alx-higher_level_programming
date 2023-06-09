#include "lists.h"

/**
 * insert_node - a func that inserts a num into a sorted linked list
 * @head: pointer to first node
 * @number: the num to be inserted
 * Return:address of new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *temp = NULL;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (curr && curr->n < number)
		{
			temp = curr;
			curr = curr->next;
		}
		temp->next = new;
		new->next = curr;
	}
	return (new);
}
