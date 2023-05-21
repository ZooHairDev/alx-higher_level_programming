#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
  Prints all integers of a list.

  Args:
    my_list: The list to print.

  Returns:
    None.
  """

  for i in my_list:
      if type(i) == int:
          print(f"{i}\n")
