# question: How many Citi Bike rides each day are taken by
# "subscribers" versus "customers"?

# answer: Choose a single day of rides to examine.
# the dataset used for this exercise was generated from the original
# Citi Bike system data found here: https://s3.amazonaws.com/tripdata/index.html
# filename: 202009-citibike-tripdata.csv.zip

# program Outline:
# 1. read in the data file: 202009CitibikeTripdataExample.csv
# 2. create variables to count: subscribers, customers, and other
# 3. for each row in the file:
#       a. If the "User Type" is "Subscriber," add 1 to "subscriber_count"
#       b. If the "User Type" is "Customer," add 1 to "customer_count"
#       c. Otherwise, add 1 to the "other" variable
# 4. print out my results

import csv

source_file = open("citybikedata.csv", "r")

citibike_reader = csv.DictReader(source_file)

subscriber_count = 0
customer_count = 0
other_user_count = 0

for row in citibike_reader:
  if row["usertype"] == "Subscriber":
    subscriber_count = subscriber_count + 1
  elif row["usertype"] == "Customer":
    customer_count = customer_count + 1
  else:
    other_user_count = other_user_count + 1

print(subscriber_count)
print(customer_count)
print(other_user_count)
