# --------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Primary Machine Learning Code
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
import time                         # for reporting how much time the functions take to finish
from sklearn.model_selection        import train_test_split                 # Required for Gradient Boosting Regressor
from sklearn                        import ensemble                         # Required for Gradient Boosting Regressor
from sklearn.metrics                import mean_absolute_error              # Required for Gradient Boosting Regressor
import statsmodels.formula.api as smf    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import print_line_of_dashes
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing, log_df_process_completed
from common                         import format_currency_total
from features                       import remove_minimal_impact_features
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Logging
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def results_model_overview( model, value_to_predict ):
    print( '' )
    # log_file_name = '1_model_overview'
    # old_stdout, log_file = log_screen_print_statements( log_file_name, sys.stdout )

    print_line_of_dashes()
    print ( 'Machine Learning Model Summary' )
    print_line_of_dashes()
    print   ( 'Gradient Boosting Regressor' )
    print_line_of_dashes()
    print   (
            str( 'n_estimators       =' ).ljust( 20, ' ' ), str( model.n_estimators     ).ljust( 5, ' ' ),
            str( 'learning_rate ='      ).ljust( 10, ' ' ), str( model.learning_rate    ).ljust( 5, ' ' ),
            str( 'max_depth ='          ).ljust( 10, ' ' ), str( model.max_depth )         
            )
    print   (
            str( 'min_samples_leaf   =' ).ljust( 20, ' ' ), str( model.min_samples_leaf ).ljust( 5, ' ' ),
            str( 'max_features  ='      ).ljust( 10, ' ' ), str( model.max_features     ).ljust( 5, ' ' ),
            str( 'loss      ='          ).ljust( 10, ' ' ), str( model.loss )                
            )
    print ( str( 'value for analysis =' ).ljust( 20, ' ' ), value_to_predict )
    print_line_of_dashes()

    # sys.stdout = old_stdout
    # print_log ( log_file, log_file_name )

def results_model_performance ( model, single_country_df, y_train, y_test, X_train, X_test, value_to_predict ): 
    print_line_of_dashes()
    print ( 'Machine Learning Model Results' )
    print_line_of_dashes()

    tab_ml = 50
    total_donations     = format_currency_total( single_country_df[ value_to_predict ].sum()    )
    mean_donations      = format_currency_total( single_country_df[ value_to_predict ].mean()   )    
    median_donations    = format_currency_total( single_country_df[ value_to_predict ].median() )  
    mean_standard_error_training_data   =  mean_absolute_error(y_train, model.predict(X_train))
    mean_standard_error_testing_data    =  mean_absolute_error(y_test,  model.predict(X_test))
    mean_standard_error_variance        =  mean_standard_error_training_data - mean_standard_error_testing_data
    
    print('Total  - Funds Raised ( local currency )'.ljust( tab_ml ), total_donations ) 
    print('Mean   - Funds Raised'. ljust( tab_ml ), mean_donations ) 
    print('Median - Funds Raised'. ljust( tab_ml ), median_donations ) 
    print('')
    print( ('Total Columns'). ljust( tab_ml ), len(single_country_df.columns) ) 
    print( ('Total Rows (records)'). ljust( tab_ml ), len(single_country_df) ) 
    print ( '' )
    print('Mean Absolute Error - TRAINING data set'.ljust( tab_ml ), format_currency_total( mean_standard_error_training_data ) )
    print('Mean Absolute Error - TESTING. data set'.ljust( tab_ml ), format_currency_total( mean_standard_error_testing_data ) )
    print('Variance between Training and Testing Data'.ljust( tab_ml ), format_currency_total( mean_standard_error_variance ) )
    print_line_of_dashes()

    # sys.stdout = old_stdout
    # print_log ( log_file, log_file_name )

def results_important_features( model, feature_labels ):
    print_line_of_dashes()
    print ( 'Feature Importance (descending order) - relative to overall importance' )
    print_line_of_dashes()

    importance = model.feature_importances_
    feature_indexes_by_importance = importance.argsort()
    for index in reversed( feature_indexes_by_importance ):
        importance_percent = str ( round( ( importance[index] * 100.0 ), 2 ) ) + ' %' 
        print (   str( feature_labels[index] ).ljust( 30 ), importance_percent)
    print_line_of_dashes()   


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Workers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def potential_feature_list( share_df ):
    function_start_time = time.time()
    log_process_commencing  ( 'determine full list of potential share features' )

    column_name_list_from_share_df = list(share_df.columns.values)
    valid_ml_feature_columns = []
    invalid_ml_feature_columns = []

    for column in column_name_list_from_share_df:
        boolean_status = 'unknown'
        column_to_assess = share_df[column].value_counts().to_frame().reset_index()
        if column_to_assess['index'].dtype == 'int64':              # Ensure that the column is actually an integer
            if len( column_to_assess ) < 3:                         # there will be 1 or 2 columns only
                check_sum = int( column_to_assess['index'].sum()  )  
                if check_sum < 2:                                   # and they should add to 0 or 1
                    boolean_status = 'is_boolean'
                else : boolean_status = 'not_a_0_1_combination'

        if boolean_status == 'is_boolean':
            valid_ml_feature_columns.append(column)
        else:
            invalid_ml_feature_columns.append(column)

    # feature_labels = np.array( valid_ml_feature_columns )

    log_df_process_completed( share_df, function_start_time )
    return ( valid_ml_feature_columns, invalid_ml_feature_columns )

def create_df_with_features_only ( share_df, features ):
    function_start_time = time.time()
    log_process_commencing  ( 'subsetting features dataframe share_df' )

    features_df = share_df[features].copy()

    log_df_process_completed( share_df, function_start_time )
    return ( features_df )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ordinary Least Squares (OLS) - Linear Regression Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def ordinary_least_squares_regression ( features_only_df, value_to_predict, feature_labels ):
    print_line_of_dashes()
    print ( 'OLS Regression Results' )
    print_line_of_dashes()

    formula_string =  str( value_to_predict + ' ~ ' )
    for feature in feature_labels:
        formula_string = formula_string + str( feature + '+' )
    formula_string = formula_string[:-1]  

    ols_result = smf.ols(formula=formula_string, data=features_only_df).fit()

    print ( ols_result.summary(), '\n' )
    print_line_of_dashes()   


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Machine Learning Code
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def gradient_boosting_regressor( features_only_df, share_df, feature_labels, value_to_predict ):
    X = features_only_df.values

    y = share_df[ value_to_predict ]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model = ensemble.GradientBoostingRegressor  (
                                                n_estimators        = 1000,
                                                learning_rate       = 0.5,
                                                max_depth           = 6,
                                                min_samples_leaf    = 9,
                                                max_features        = 0.1,
                                                loss                = 'huber'
                                                )
    model.fit(X_train, y_train)

    #---------------------------------------------------------- Report on Model Performance
    results_model_overview( model, value_to_predict )
    results_model_performance( model, share_df, y_train, y_test, X_train, X_test, value_to_predict )
    results_important_features( model, feature_labels )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager Function
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def machine_learning_manager( share_df, value_to_predict ):
    core_process_name           = 'Generate Machine Learning Model'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    valid_ml_feature_columns, invalid_ml_feature_columns = potential_feature_list( share_df)
    # print ( 'Valid Feature List' )
    # print ( valid_ml_feature_columns )
    # print ( 'In Valid Feature List' )
    # print ( invalid_ml_feature_columns )


    # features  = remove_multi_collinearity_features( features )
    features  = remove_minimal_impact_features    ( valid_ml_feature_columns, share_df )
    features  = sorted( features )

    features_only_df = create_df_with_features_only( share_df, valid_ml_feature_columns )


    gradient_boosting_regressor( features_only_df, share_df, valid_ml_feature_columns, value_to_predict )

    ordinary_least_squares_regression ( share_df, value_to_predict, valid_ml_feature_columns )




    log_core_process_footer( core_process_name, core_process_start_time )


