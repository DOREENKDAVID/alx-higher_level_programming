#include "lists.h"


/**
 * check_cycle - a func that checks if a singlylinked list has a cycle in it
 * @list:linked list to be checked
 * Return:1 if it has and 0 if it does not
 */

int check_cycle(listint_t *list);
{
	listint_t *head = list;
	listint_t *tail = list;

	if (!list)
		return (0);

	while (head && tail && head->next)
	{
		head = head->next->next;
		tail = tail->next;
		if (tail == head)
			return (1);
	}
	return (0);
}
