#include "lists.h"

/**
 * insert_node - insert a node into a sorted singly linked list
 *
 * @head: head of the linked list
 * @number: the number to insert
 *
 * Return: address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curr, *prev;

	if (head == NULL || *head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	curr = *head;
	while (curr)
	{
		if (curr->n > new->n)
		{
			new->next = curr;
			prev->next = new;
			break;
		}
		prev = curr;
		curr = curr->next;
	}
	return (new);
}
