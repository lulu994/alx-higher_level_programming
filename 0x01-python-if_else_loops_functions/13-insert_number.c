#include "lists.h"

/**
  *insert_node - Inserts a number into a sorted singly-linked list
  * @head: A pointer the head of the linked list.
  * @number: The number to insert.
  * Return: If the function fails - NULL
  * Otherwise - a pointer to the new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node;
	if (head == NULL)
		return(NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	current_node = *head;
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return(new_node);
	}
	if (current_node->n > number)
	{
		new_node->next = current_node;
		*head = new_node;
		return(new_node);
	}
	
	while (current_node->next != NULL)
	{
		if(current_node->next->n > number)
		{
			new_node->next = current_node->next;
			current_node->next = new_node;
			return(new_node);
		}
		current_node = current_node->next;
	}
	current_node->next = new_node;
	return(new_node);
}
