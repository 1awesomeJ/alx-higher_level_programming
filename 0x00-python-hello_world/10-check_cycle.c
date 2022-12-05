#include "lists.h"
#include <stdio.h>

int check_cycle(listint_t *list)
{
   	listint_t *temp, *check, *current;
    	int i,j;
	if (list == NULL)
		return (0);
	temp = current = list;
 	i = j = 0;

	while (current->next != NULL)
	{
		check = current->next;
		while ( temp->next != NULL)
		{
		if (((temp->next == check) && i != j) || (temp->next == list))
				return (1);
		temp = temp->next;
		j++;
		}
		current = current->next;
		temp = list;
		j= 0;
		i++;
	}
		return(0);
}
