# What happens when two variables in the dataset are correlated?

# Introduce a little anarchy

input_data['atemp_dummy'] = input_data['atemp'].apply(lambda x:\
                              x * 2)

# Check that the two variables are indeed correlated!
  ## Observe non-principal diagonal elements of the matrix
np.corrcoef(input_data['atemp'], input_data['atemp_dummy'])

# But how does it affect the linear regression score?
simple_linreg_model_cor = linear_model.LinearRegression()

# Build a model using the two variables

simple_linreg_model_cor.fit(input_data[['humidity', 'atemp', 'atemp_dummy']], \
                            input_data[['casual_log']])

# What is the intercept fit?
simple_linreg_model_cor.intercept_
# Compare it with average of data using input_data['casual'].mean()

# What are the co-efficients fit?
simple_linreg_model_cor.coef_
# Can you spot a difference with previous value?

# Check the performance
simple_linreg_cor_mse = metrics.mean_squared_error(input_data['casual_log'],
                             simple_linreg_model_cor.predict\
                             (input_data[['humidity', 'atemp', 'atemp_dummy']]))

print simple_linreg_mse
print simple_linreg_cor_mse

# Are you surprised by the result? We thought co-linearity was bad!
  ## Then what is bad with co-linearity?
