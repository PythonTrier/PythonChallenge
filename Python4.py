#Used to make requests
import urllib.request
import re

r = r'[0-9]*$'
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
next_nothing = "12345"
#next_nothing = "8022"
previous_nothing=0

# range(start, stop, step)
for i in range(1, 400, 1):
  x = urllib.request.urlopen(base_url + next_nothing)
  response_nothing = x.read().decode("utf-8")
  next_nothing = re.findall(r, response_nothing)[0]

  if next_nothing.isdigit() != True:
    print("STOP! {0}".format(response_nothing))
    print("Your last nothing is: {0}".format(previous_nothing))
    next_nothing = input("Enter your next nothing or 'exit' to quit: ")
    if next_nothing == "exit":
      print("Goodbye!")
      break

  else:
    previous_nothing=next_nothing
    print("Next nothing: {0} at index {1}".format(next_nothing, i))


#peak.html