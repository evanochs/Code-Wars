# My Soltion

# def comp(array1, array2):
#     print(array1)
#     print(array2)
#     status = True
#     if type(array1) == list and type(array2) == list:
#         if len(array1) == len(array2):
#             if len(array1) == 0 or len(array2) == 0:
#                 return True
#             if len(array1) <= 1 or len(array2) <= 1:
#                 return False
#             else:
#                 for x in range(len(array1)):
#                     current_number = (array1[x])**2
#                     if current_number in array2:
#                         array2.remove(current_number)
#                         continue
#                     else:
#                         status = False
#                         break
#                 return status
#         else:
#             return False
#     if type(array1) == list and not array2:
#         return False
#     else:
#         return False

# CodeWars best solution

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

