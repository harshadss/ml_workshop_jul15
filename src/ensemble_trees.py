from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor(loss = 'ls',
                                min_samples_split = 10)

gbr.fit(train_data.drop(target, axis = 1),
                train_data['casual_log'])

gbr_mse_train = metrics.mean_squared_error(
                                  train_data['casual_log'],
                                  gbr.predict\
                                  (train_data.drop(target, axis =1 )) )

gbr_mse_test = metrics.mean_squared_error(
                                  test_data['casual_log'],
                                  gbr.predict\
                                  (test_data.drop(target, axis =1 )) )

