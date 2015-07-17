# Contains codes related to bias-var tradeoff, validations, regularizations.

# First split the data between training and testing
from sklearn.cross_validation import train_test_split

(train_data, test_data) = train_test_split(relevant_data, test_size = 0.3,
                                         random_state = 42)

feature_engg_linreg_model.fit(train_data.drop(target, axis = 1),
                        train_data['casual_log'])

feature_engg_linreg_mse_train =\
                        metrics.mean_squared_error(
                            train_data['casual_log'],
                        feature_engg_linreg_model.predict\
                        (train_data.drop(target, axis = 1) ) )

feature_engg_linreg_mse_test =\
                        metrics.mean_squared_error(
                            test_data['casual_log'],
                        feature_engg_linreg_model.predict\
                        (test_data.drop(target, axis = 1) ) )


# Not much difference? > Doesn't look like we are overfitting!

# But how to perform shrinkage/penalized regression in general?

from sklearn.linear_model import LassoCV

feature_engg_lassocv_model = LassoCV(max_iter = 50, cv= 3,
                               n_jobs = -1, random_state = 42)

feature_engg_lassocv_model.fit(train_data.drop(target, axis = 1),
                        train_data['casual_log'])

feature_engg_lassocv_mse_train = metrics.mean_squared_error(
                                  train_data['casual_log'],
                                  feature_engg_lassocv_model.predict\
                                  (train_data.drop(target, axis =1 )) )

feature_engg_lassocv_mse_test = metrics.mean_squared_error(
                                  test_data['casual_log'],
                                  feature_engg_lassocv_model.predict\
                                  (test_data.drop(target, axis =1 )) )


# Check the performance on test set
print feature_engg_linreg_mse_test
print feature_engg_lassocv_mse_test
# Penalization decreases performance?

# Compare coefficients with non penalized model
print feature_engg_linreg_model.coef_[1:10]
print feature_engg_lassocv_model.coef_[1:10]
