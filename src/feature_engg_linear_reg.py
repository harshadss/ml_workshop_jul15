from sklearn import linear_model

feature_engg_linreg_model = linear_model.LinearRegression()

# Build a model using the two variables

feature_engg_linreg_model.fit(relevant_data.drop(target, axis = 1),
                        relevant_data[['casual_log']])

feature_engg_linreg_r2_training =\
                        feature_engg_linreg_model.score\
                        (relevant_data.drop(target, axis = 1),
                        relevant_data[['casual_log']])

feature_engg_linreg_mse = metrics.mean_squared_error(relevant_data['casual_log'],
                          feature_engg_linreg_model.predict\
                                     (relevant_data.drop(target, axis = 1)) )

# Have we improved by adding features?
print simple_linreg_mse
print simple_linreg_cor_mse
print feature_engg_linreg_mse
