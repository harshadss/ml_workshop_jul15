# Exploring the dataset

# Basic stats at dataset level

print input_data.shape
print input_data.columns

# Target variables are casual and registered

print input_data['casual'].describe()
print input_data['registered'].describe()

# Standard deviation of casual Vs. registered, is there a difference?
# If yes, why would be the difference? Is it expected?

# Exploring other variables

# Is the data uniform? What is the duration?
input_data['datetime'].describe()
# Are the date times repeated? How do you conclude from above output?

# Check humidity
input_data['humidity'].describe()
# Do we need a scaling of this column? Why / Why Not?

# Repeat the process to explore other variables
input_data['season'].describe()
# Do we have enough data from each season?
input_data['season'].value_counts()

# Repeat the process to explore other variables

# Simple data transformation: log transform the target vars
  ## This is derived from competition target
  ## In an ideal world, we can fit count regression models like Python on data
import math
input_data['casual_log'] = input_data['casual'].apply(lambda x: math.log(x + 1))
input_data['registered_log'] = input_data['registered'].apply(lambda x: math.log(x + 1))

