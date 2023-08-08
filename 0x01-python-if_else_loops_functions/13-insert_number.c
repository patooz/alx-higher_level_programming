#include "lists.h"

/**
 * insert_node - inserts a number to singly list
 * @head: pointer to the singly list
 * @number: inserted number
 * Return: NULL on failure, pointer on success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *data = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (data == NULL || data->n >= number)
	{
		new->next = data;
		*head = new;
		return (new);
	}
	while (data && data->next && data->next->n < number)
		data = data->next;
	new->next = data->next;
	data->next = new;
	return (new);
}
