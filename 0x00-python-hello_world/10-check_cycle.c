#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0

 /**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to the first element of a linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;//Creates two separate pointers, slow and fast, and assigns them to the pointer passed to the function.
     if (!list)//If the pointer passed is NULL
        return (FALSE);//then the function will return FALSE
     while (fast && fast->next)//check if the fast pointer is not NULL and the next pointer of the fast pointer is also not NULL
    {
        slow = slow->next;//slow pointer is then incremented to the next pointer in the list
        fast = fast->next->next;//The fast is incremented twice to the next next pointer in the list
         if (slow == fast)//checks if the slow and fast pointers are equal
            return (TRUE);//Return true which means there is circle in the list
    }
     return (FALSE);
}
//CodeLord
