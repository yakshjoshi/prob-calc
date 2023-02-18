import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents += v * [k]

  def draw(self, num):
    
    if num > len(self.contents):
      return self.contents
    else:
      new_list = random.sample(self.contents, num)

      for i in new_list:
        self.contents.remove(i)
   
    return new_list
    




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  probability = 0.0
  favourable_outcome = 0
  ex_list = []
  for k, v in expected_balls.items():
      ex_list += v * [k]

  for i in range(num_experiments):
    outcome = copy.deepcopy(hat)
    new_outcome = outcome.draw(num_balls_drawn)

    dict1 = Counter(new_outcome)

    if all(dict1[k] >= v for k, v in expected_balls.items()):
      favourable_outcome+=1
      
        
    #dict1 = Counter(ex_list)
    #ict2 = Counter(su_nu)
    
    #if dict1 == dict2:
     # favourable_outcome +=1
 
  probability = favourable_outcome/num_experiments
  
  return probability



    
    
  