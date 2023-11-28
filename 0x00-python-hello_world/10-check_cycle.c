#include "lists.h"

/**
 * check_cycle - check if list is cycled
 * @list: pointer input
 * Return: 1 if yes, 0 if  no
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

