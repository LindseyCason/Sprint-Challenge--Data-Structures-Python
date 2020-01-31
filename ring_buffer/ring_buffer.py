from doubly_linked_list import DoublyLinkedList
#U:
#There is a limited capacity for the array you are give and it is passed in through RingBuffer(capacity). When the cap is met, we should overwrite the first/oldest element in the list. Never exceeding the cap. Current, which should be the position we're at is set to None. May use this as a counter and/or index as we're increasing through the array, possibly the oldest index in the array.. We're also given storage which links us to DoublyLinkedList which gives us these methods.add_to_head(value)
# remove_from_head()
# add_to_tail(value)
# remove_from_tail()
# move to front(node) -these delete the node upon moving to front
# move to end(node)-deletes node.
#MIGHT BE ALL WE CAN USE HERE- delete(node)
# get_max()
#Things we cant do: Cannot use a list[] in the append method. Cannot allow "None" to print

#P:
#If there is no Node, add one and set it to current. This will be the oldest item
#if we're not at capacity, add items to the tail until we are at capacity
#if we are at cap (check len vs cap).
  #if current is not at the end of the line(curr == tail), make the next value= to the item we're adding, reassign curr to the curr.next. This moves current up a notch and will now be on the oldest node. We do this every time we add something when we're == cap.
#get-
  #

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None #THIS IS LIKE AN INDEX
        self.storage = DoublyLinkedList()

    def append(self, item):
      if self.current == None:
        #if there is no item in the DLL, this makes one and adds it, the one added is set to the current oldest item
        self.storage.add_to_tail(item)
        self.current=self.storage.head
        print(self.current.value)
        #set the current to the head
        return      

      if self.capacity <= len(self.storage): #LESS THAN OR == NOT GREATER THAN OR ==
        #if we have no more room...
        if self.current != self.storage.tail:#and the current does NOT == the tail(BECAUSE WHEN WE HIT THE CURRENT == TAIL WE'RE AT THE END OF THE ARRAY)

          self.current.next.value=item #change the value of the NEXT
          # print("current",self.current.value)
          # print("current NEXT",self.current.next.value)
          self.current=self.current.next #set current to it's current next, this keeps current the oldest item

        else: #if current is == tail at the end of the line
          self.current = self.storage.head#change current to current head (moves back to the beginning)
          self.current.value=item #make the value the item
          #this brings it back to the beginning so we can keep going

      else:
        #if we aren't at capacity
        self.storage.add_to_tail(item)#adding to tail
        self.current=self.current.next#movin on up

    def get(self):
        # Note:  This is the only [] allowed
      list_buffer_contents = []
      head=self.storage.head
      while head: #while a head exists, this eliminates the initial None
        #Go through the list and append each head item to the LBC array.
        list_buffer_contents.append(head.value)
        head=head.next #this moves to the next node so the loop can start appending from there until the end
      return list_buffer_contents
      #when done looping, return the array

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
