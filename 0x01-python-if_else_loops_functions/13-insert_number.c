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
	listint_t *new, *curr;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	curr = *head;
	if (curr == NULL || curr->n >= number)
	{
		new->next = curr;
		*head = new;
		return (new);
	}

	while (curr && curr->next && new->n > curr->next->n)
		curr = curr->next;

	new->next = curr->next;
	curr->next = new;
	return (new);
}
