#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle in it
 *
 * @list: the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast;

	if (list == NULL)
		return (0);
	fast = list->next;
	while (fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
