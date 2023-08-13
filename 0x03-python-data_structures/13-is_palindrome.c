#include "lists.h"

/**
 * is_palindrome - checks if the linked list ia a palindrome
 * @head: pinter to the linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *t = *head, *d = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			d = s->next;
			break;
		}
		if (!f->next)
		{
			d = s->next->next;
			break;
		}
		s = s->next;
	}
	back_int(&d);
	while (d && t)
	{
		if (t->n == d->n)
		{
			d = d->next;
			t = t->next;
		}
		else
			return (0);
	}
	if (!d)
		return (1);
	return (0);
}
/**
 * back_int - reverses the linked list
 * @head: pointer to the linked list
 * Return: pointer to the node
 */
void back_int(listint_t **head)
{
	listint_t *p = NULL;
	listint_t *now = *head;
	listint_t *next = NULL;

	while (now)
	{
		next = now->next;
		now->next = p;
		p = now;
		now = next;
	}
	*head = p;
}
