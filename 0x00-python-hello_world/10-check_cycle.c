#include "lists.h"

int check_cycle(listint_t *list)
{

   	listint_t *temp, *check;
    	int i, len;
	temp = list;
    	len = 0;
    	while (list != NULL)
	   {
		   list = list->next;
			   len++;
	   }
	list = temp;
	while (list != NULL)
	{
	check = list->next;
	for (i = 0; i < len; i++)
	{
		list = list->next;
		if (list->next == check)
			return (1);
		if (list->next == NULL)
			return (0);
	}
	list = check;
	}
	list = temp;
	
	return(1);
}
