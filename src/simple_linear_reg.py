# We assume casual users will take a call based on humidity and temperature
# This forms our hypothesis.

from sklearn import linear_model

simple_linreg_model = linear_model.LinearRegression()

# Build a model using the two variables

simple_linreg_model.fit(input_data[['humidity', 'atemp']], input_data['casual_log'])

# What is the intercept fit?
simple_linreg_model.intercept_
# Compare it with average of data using input_data['casual'].mean()

# What are the co-efficients fit?
simple_linreg_model.coef_

# Do you agree with the signs of the co-efficients?
# Which one looks odd? Can we think of it in conjuction with intercept?

# Check the performance
print simple_linreg_model.score(input_data[['humidity', 'atemp']], 
                                input_data['casual_log'])

# But which score is this?
help(simple_linreg_model.score)

# What is the logic of comparing with average value?
# What are typical problems with simple R^2 measure?

# Store the score in var for later reference
simple_linreg_r2 = simple_linreg_model.score(\
                                input_data[['humidity', 'atemp']],
                                input_data['casual_log'])

# r^2 may not be a good measure, gets inflated

from sklearn import metrics

print simple_linreg_mse = metrics.mean_squared_error(input_data['casual_log'],
                    simple_linreg_model.predict\
                                     (input_data[['humidity', 'atemp']]))
