from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return str(self.val)


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
        Find and return the middle node of the linked list.
    """
    nodes = []

    def explore_list(node, nodes_nb=nodes):
        """
            Explore the linked list
            and update its mutable default argument <nodes_nb>
            to know the list depth/length outside the function.
        """
        nodes_nb.append(1)

        if node.next is None:
            return
        else:
            explore_list(node.next)

    explore_list(head)

    list_len = len(nodes)

    nodes = []
    middle = []

    def find_middle(node, counter=nodes, length=list_len, res=middle):
        """
            Explore the linked list
            and insert its middle to the mutable argument <res> when detected,
            that will be gotten outside the function.
        """
        counter.append(1)

        if len(counter) == (length // 2) + 1:
            # Middle node found !
            res.append(node)
            return

        if node.next is None:
            return
        else:
            find_middle(node.next)

    find_middle(head)

    return middle.pop()


def is_palindrome(head: Optional[ListNode]) -> bool:
    """
        Check if a linked list is a palindrome.
    """
    nodes_vals = []

    def explore_list(node, vals=nodes_vals):
        vals.append(node.val)

        if node.next is None:
            return
        else:
            explore_list(node.next)

    explore_list(head)

    return nodes_vals == nodes_vals[::-1]


linked_list = ListNode(
    val=1,
    next_node=ListNode(
        val=2,
        next_node=ListNode(
            val=3, next_node=ListNode(
                val=4, next_node=ListNode(val=5, next_node=None)
            )
        )
    )
)

print(middle_node(linked_list))
