# Module for performing support vector regression

from sklearn.svm import SVR

# Simple svr with fixed parameters and linear kernel

svr_lin = SVR(kernel = 'linear', C = 10, max_iter = 100)

svr_lin.fit(train_data.drop(target, axis = 1),
                        train_data['casual_log'])

# svr with fixed params, rbf kernel
svr_rbf = SVR(kernel = 'rbf', C = 10, gamma = 0.1, max_iter = 100)
svr_rbf.fit(train_data.drop(target, axis = 1),
                        train_data['casual_log'])

# Check the performance
svr_lin_mse_train = metrics.mean_squared_error(train_data['casual_log'],
                        svr_lin.predict(train_data.drop(target, axis = 1)))

svr_lin_mse_test = metrics.mean_squared_error(test_data['casual_log'],
                        svr_lin.predict(test_data.drop(target, axis = 1)))

svr_rbf_mse_train = metrics.mean_squared_error(train_data['casual_log'],
                        svr_rbf.predict(train_data.drop(target, axis = 1)))

svr_rbf_mse_train = metrics.mean_squared_error(test_data['casual_log'],
                        svr_rbf.predict(test_data.drop(target, axis = 1)))

# Print
print svr_lin_mse_train, svr_lin_mse_test
print svr_rbf_mse_train, svr_rbf_mse_test

