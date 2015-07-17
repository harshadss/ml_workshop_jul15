# Module for performing simple tree regression

from sklearn.tree import DecisionTreeRegressor

simple_tree = DecisionTreeRegressor()

simple_tree.fit(train_data.drop(target, axis = 1),
                train_data['casual_log'])

simple_tree_mse_train = metrics.mean_squared_error(
                                  train_data['casual_log'],
                                  simple_tree.predict\
                                  (train_data.drop(target, axis =1 )) )

simple_tree_mse_test = metrics.mean_squared_error(
                                  test_data['casual_log'],
                                  simple_tree.predict\
                                  (test_data.drop(target, axis =1 )) )

# How does the result compare with SVR and linear models?

# DTrees can easily overfit!

pruned_tree = DecisionTreeRegressor(min_samples_split = 10,
                                    min_samples_leaf = 5,
                                    max_depth = 6)

pruned_tree.fit(train_data.drop(target, axis = 1),
                train_data['casual_log'])

pruned_tree_mse_train = metrics.mean_squared_error(
                                  train_data['casual_log'],
                                  better_tree.predict\
                                  (train_data.drop(target, axis =1 )) )

pruned_tree_mse_test = metrics.mean_squared_error(
                                  test_data['casual_log'],
                                  better_tree.predict\
                                  (test_data.drop(target, axis =1 )) )
