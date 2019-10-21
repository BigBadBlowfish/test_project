class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def list_length(self):
        list_len = 0
        current_node = self.head_node
        while current_node is not None:
            list_len += 1
            current_node = current_node.next_node
        return list_len
    
    def add_list_item(self, item):
        if isinstance(item, ListNode):
            if self.head_node is None:
                self.head_node = item
                self.tail_node = item
                item.prev_node = None
                item.next_node = None
            else:
                self.tail_node.next_node = item
                item.prev_node = self.tail_node
                self.tail_node = item
        return



class ListNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

    def has_next_node(self):
        if self.next_node != None:
            return True
        else:
            return False

    def get_next_node(self):
        if self.next_node != None:
            return self.next_node
        else:
            return None
    
    def get_prev_node(self):
        if self.prev.node != none:
            return self.prev_node
        else:
            return None

    def has_value(self, value):
        if value == self.data:
            return True
        else:
            return False