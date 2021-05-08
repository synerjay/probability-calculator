import copy
import random
# Consider using the modules imported above.

class Hat:
    # **balls is an arbitrary number of arguments and are treated like a dictionary
    def __init__(self, **balls):
      self.contents = list()
      for (k, v) in balls.items():
        for x in range(v):
          self.contents.append(k)
    
    def draw(self, num):
      if num > len(self.contents):
        return self.contents
      else:
        out = list()
        for x in range(num):
          out.append(self.contents.pop(random.randrange(len(self.contents))))
        return out


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0

    # make for loop 
    for i in range(num_experiments):
      # make a copy of each iteration of Hat
      fake = copy.deepcopy(hat)

      # make a dictionary for drawn balls 
      drawn_balls = fake.draw(num_balls_drawn)
      drawn_dict = dict()
      # get the histogram .get() method 
      for ball in drawn_balls:
        drawn_dict[ball] = drawn_dict.get(ball, 0) + 1

      # check to see how many successes in each iteration

      check = True
      for (k,v) in expected_balls.items():
        if k not in drawn_dict.keys() or drawn_dict[k] < expected_balls[k]:
          check = False
          break

      if check:
        success = success + 1
    
    return success / num_experiments
