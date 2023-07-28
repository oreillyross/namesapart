def split_name_three_plus(names):
  first_names = []
  last_names = []

  for i, name in enumerate(names):
    if i == len(names) - 1:
      last_names.append(name)
    elif name[0].islower():
      last_names.extend(names[i:])
      break
    else:
      first_names.append(name)
  first_name = " ".join(first_names)
  last_name = " ".join(last_names)
  return [first_name, last_name]

  
def split_name(name):

  names = name.split(" ")
  
  if not names:
    return ["", ""]
 
  if len(names) == 1:
    return ["", names[0]]
   
 
  if len(names) == 2:
    first_name, last_name = names
    return [first_name, last_name]
  else:
    return split_name_three_plus(names)