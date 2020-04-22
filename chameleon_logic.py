class Chameleon:

  #every even number mod 2 is always 0
  def isEven(self, num):
    return num%2 == 0

 #simply looping through each character
 #to check if it is equal to the given char
  def count(self, string, c):
    counter = 0
    for char in string:
      if (char == c):
        counter+=1
    return counter

  # going through the first array and 
  # checking if each element is present in the second
  def findIntersection(self, arr1, arr2):
    intersect = []
    for element in arr1:
      if element in arr2:
        intersect.append(element)
    
    return intersect

def main():
  c = Chameleon()
  print(c.isEven(11))
  print(c.count("hello", 'l'))
  print(c.findIntersection([1,2,3], [2,4,5,1]))
  
if __name__ == "__main__":
  main()

