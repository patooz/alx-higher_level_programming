#include "lists.h"

/**
 * check_cycle - check for loop in linked list
 * @list: head of the linked lis
 * Description - check if there is a loop in liked list
 * Return: 1 if present, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (!list)
		return (0);
	s = list;
	f = list->next;
	while (f && s && f->next)
	{
		if (s == f)
			return (1);
		s = s->next;
		f = f->next->next;
	}
	return (0);
}
