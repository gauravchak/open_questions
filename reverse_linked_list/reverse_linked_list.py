def reverse_iterative(head):
  '''Reverse a list'''
  if (head == None) or (head.next == None):
    # Nothing to do since it has 0 or 1 element
    reversed_list = head
  
  new_next = None
  old_next = head.next
  current_elem = head
  while (current_elem.next != None):
    # Save the forward element ref in old_next
    old_next = current_elem.next
    current_elem.next = new_next
    # Save the current element in variable new_next so that we can set it in the next iteration.
    new_next = current_elem
    # Move to the forward element in the next iteratio
    current_elem = old_next
  # On exiting loop the last element should be the new head, except that we should not forget 
  # to reverse the next pointer of this element
  current_elem.next = new_next
  reversed_list = current_elem
  return reversed_list
