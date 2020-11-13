from concurrent.futures import ThreadPoolExecutor
import names
import json

from random import randint

#Generate the N dig number function
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#Dictionary for storing the names and phone numbers
data=dict()

# Phone number generator function with proper prefix
def phone_number_generator():
  arr=["6","7","8","9"]
  for mciNumbers in range(0,50):
    temp=randint(0,3)
    data[names.get_full_name()]= '+91 ' + arr[temp]+ str(random_with_N_digits(9))

def main():
  with ThreadPoolExecutor() as executor:
    task1 = executor.submit(phone_number_generator())
    task2 = executor.submit(phone_number_generator())
    task3 = executor.submit(phone_number_generator())
    task4 = executor.submit(phone_number_generator())


import time
start = time.time()

if __name__ =='__main__':
  main()

file = open('phoneNumbers.json','w')
json_object=json.dumps(data,indent=8)
file.write(json_object)
file.close()

end = time.time()
print(end - start)

