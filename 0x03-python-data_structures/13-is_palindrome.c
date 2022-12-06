#include "lists.h"

/**
 * find_middle - find the middle of a linked list
 *
 * @head: the head of the list
 *
 * Return: the middle element of the list
 */
listint_t *find_middle(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}

/**
 * reverse_list - reverse a linked list
 *
 * @head: the grass of the list
 *
 * Return: the head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *ptr = head, *temp, *prev = NULL;

	while (ptr)
	{
		temp = ptr->next;
		ptr->next = prev;
		prev = ptr;
		ptr = temp;
	}
	return (prev);
}

/**
 * is_palindrome - check if a linked list is a palindrome
 *
 * @head: the head of the linked list
 *
 * Return: 1 if palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle, *reversed_half;
	listint_t *ptr1, *ptr2;

	middle = find_middle(*head);
	reversed_half = reverse_list(middle);

	ptr1 = *head;
	ptr2 = reversed_half;
	while (ptr1 && ptr2)
	{
		if (ptr1->n != ptr2->n)
		{
			reverse_list(reversed_half);
			return (0);
		}
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	reverse_list(reversed_half);
	return (1);
}
