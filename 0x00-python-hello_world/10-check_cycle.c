#include "lists.h"

/**
 * check_cycle - Write a function in C that checks if a singly linked list
 * has a cycle in it.
 *
 * @list: This is the input linked list
 *
 * Return:  0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

		if (slow_p == fast_p)
		{
			return (1);
		}
	}
	return (0);
}
