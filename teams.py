# SWDV 630 - Object-Oriented Software Architecture
# Added __contains__ and __iter__ to Teams class

class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)
  
  def __contains__(self, item):
    return item in self.__myTeam
  
  def __iter__(self):
    for member in self.__myTeam:
      yield member

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  
  print (len(classmates))                 # -> 3
  print('Tim' in classmates)              # -> True
  print('Sam' in classmates, '\n')        # -> False

  for member in classmates:
    print('Hello from', member)

if __name__ == '__main__': main()