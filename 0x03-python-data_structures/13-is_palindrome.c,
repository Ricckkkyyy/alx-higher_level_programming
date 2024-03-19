#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL;
    listint_t *mid = NULL, *second_half = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    second_half = slow;
    prev->next = NULL;
    reverse_list(&second_half);

    is_palindrome = compare_lists(*head, second_half);

    reverse_list(&second_half);

    if (mid != NULL)
    {
        prev->next = mid;
        mid->next = second_half;
    }
    else
        prev->next = second_half;

    return (is_palindrome);
}
