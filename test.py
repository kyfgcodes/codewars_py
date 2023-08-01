def warn_the_sheep(queue):
   wolf = queue.index('wolf')
   sheep = 0 

   if wolf == -1:
      return 'Pls go away and stop eating my sheep.'

   for i in reversed(queue):
    if i == 'wolf':
      return f"Oi sheep number {sheep +1}! You are about to be eaten by a wolf!"
      if i == 'sheep':
         sheep += 1
   
   print(wolf)
   # if wolf == -1:
   #    return "Pls go away and stop eating my sheep."
   






print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep']))