def consecutive_ints(*nums):
  """Takes any number of integer arguments and returns them in a sorted list if they can be arranged in a consecutive order.
  
  Otherwise raises a custom TypeError or ValueError.
  """
  is_list_valid = True #will be used to return the final results
  
  type_error_variable = False #will be used to avoid printing original error
  value_error_variable = False

  #checking if there are strings:
  try:
    lst = sorted(nums)
  except: 
    type_error_variable = True
   

  else: #checking for boolean and floats: 
    for i in range(len(nums)):
      if type(nums[i]) != int: 
        is_list_valid = False
        type_error_variable = True
      elif type(nums[i]) == int:
        continue
       
 
    #checking if all integers are consecutive:
    if is_list_valid == True:
      lst = sorted(nums)
      for i in range(len(lst)-1):
        if lst[i] + 1 == lst[i+1]:
          continue
        elif lst[i] + 1 != lst[i+1]:
          value_error_variable = True
          is_list_valid = False

  #---------------outputs:---------------
  if type_error_variable == True:
     raise TypeError("The inputs must be integers.")

  if value_error_variable == True:
    raise ValueError("The inputs must be arrangeable in consecutive order.")
    
  if is_list_valid == True:
    lst = sorted(nums)
    return(lst)
    


# Include at least three tests here that should return a list
print(consecutive_ints(4, 1, 3, 2))
print(consecutive_ints(40, 41, 43, 42))
print(consecutive_ints(100, 101, 102, 103, 104, 105))
print(consecutive_ints(401, 402, 403, 404))
print(consecutive_ints())


try:
  print(consecutive_ints(4, 1, 3, 2, "lol"))
except TypeError:
  print("This raises a TypeError.")
except:
  print("This raises the wrong error.")

try:
  print(consecutive_ints(4, 1, 3, 2, 5, 6, 7, 9, 10))
except ValueError:
  print("This raises a ValueError.")
except:
  print("This raises the wrong error.")