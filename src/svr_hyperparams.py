# SVR algorithms are generally sensitive to scaling of input data

# Most of the vars are in the range 0-1, except numeric vars. We
# can scale those.

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
numeric_array_sc = scaler.fit_transform(input_data[numeric_vars])
numeric_df_sc = pd.DataFrame(numeric_array_sc,
                                 columns = numeric_vars)

relevant_data_sc = pd.concat([numeric_df_sc ,
                            input_data[bool_vars],
                            cat_vars_df,
                            input_data[target] ], axis = 1)

# Train-test split again
(train_data_sc, test_data_sc) = train_test_split(relevant_data_sc, test_size = 0.3,
                                         random_state = 42)

from sklearn import grid_search

params = {'C' : [0.1, 0.5], 'gamma' : [0.1, 0.5]}

svr_rbf_hyper = SVR(kernel = 'rbf', max_iter = 500)

svr_tuned = grid_search.GridSearchCV(svr_rbf_hyper, params, n_jobs = -1)

svr_tuned.fit(train_data_sc.drop(target, axis = 1),
                        train_data_sc['casual_log'])

# Check the performance
svr_rbf_tune_mse_train = metrics.mean_squared_error(train_data_sc['casual_log'],
                        svr_tuned.predict(train_data_sc.drop(target, axis = 1)))

svr_rbf_tune_mse_test = metrics.mean_squared_error(test_data_sc['casual_log'],
                        svr_tuned.predict(test_data_sc.drop(target, axis = 1)))

# Print
print feature_engg_lassocv_mse_test
print svr_rbf_mse_test
print svr_rbf_tune_mse_test

# Are the results surprising?

# Letting it run for convergence with max_iter = -1, takes time but helps!
