# Creating simple features first

## How to use time information? We expect time of day to play a role.

input_data['hour_of_day'] = input_data['datetime'].dt.hour.\
                            apply(lambda x: str(x))

## Might also transform to sessions in day.

## People (esp. casual) might make start of year/month resolution.

input_data['month_start_bool'] = input_data['datetime'].dt.is_month_start
input_data['month_start'] = input_data['month_start_bool'].apply(lambda x:
                              1 if x else 0)

# Check if it actually helps?
print input_data.groupby('month_start_bool')['casual'].mean()
# OMG! It's actually the other way round.

input_data['year_start_bool'] = input_data['datetime'].dt.is_year_start
input_data['year_start'] = input_data['year_start_bool'].apply(lambda x:
                              1 if x else 0)

# Creating complex features to add extra information

## Season is given by 4 unique values
print input_data['season'].value_counts()
## Weather is given by 4 unique values with 1 outlier!
print input_data['weather'].value_counts()

## But probably we can have more fine grained description
## Bin temperature, wind speed and humidity and create cartesian product

input_data['humidity_bin'] = pd.qcut(input_data['humidity'], 3,\
                                     labels = ['h_low', 'h_med', 'h_high'] )

input_data['atemp_bin'] = pd.qcut(input_data['atemp'], 3,\
                                     labels = ['t_low', 't_med', 't_high'] )

input_data['windspeed_bin'] = pd.qcut(input_data['windspeed'], 3,\
                                     labels = ['w_low', 'w_med', 'w_high'] )

# Note: axis = 1 is required while operating on multi-columns
input_data['complex_season'] = input_data[['humidity_bin', 'atemp_bin',
                                           'windspeed_bin']].\
                               apply(lambda x: x['humidity_bin'] + ' ' + \
                                               x['atemp_bin'] + ' ' + \
                                               x['windspeed_bin'], axis = 1)

## How does it actually affect?

print input_data.groupby('complex_season')['casual'].mean()

## Some of them are counter intuitive. Higher temp. consistently shows higher
## values always. But remember, the data is from a foreign country. Check the
## mean value in high bin for actual temperature (not felt one)! So higher
## temperatures are actually more pleasant for bike?
print input_data.groupby(['atemp_bin'])['temp'].mean()

# Handle categorical to numeric transformation

cat_vars_df = pd.get_dummies(input_data[['hour_of_day', 'complex_season']])

# Check if all is well: 24 hours + 27 season/weather vars
print cat_vars_df.shape

# Create final usable data frame

numeric_vars = ['atemp', 'humidity', 'windspeed']
bool_vars = ['holiday', 'workingday', 'month_start', 'year_start']
target = ['casual_log', 'registered_log']

# Above vars from original data + dummied categorical vars

relevant_data = pd.concat([ input_data[numeric_vars] ,
                            input_data[bool_vars],
                            cat_vars_df,
                            input_data[target] ], axis = 1)

# What do we have now?
print relevant_data.shape

print relevant_data.columns
