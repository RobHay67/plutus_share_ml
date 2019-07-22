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
# import statsmodels.formula.api as smf    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import print_line_of_dashes
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing, log_df_process_completed
from common                         import format_currency_total

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Reporting Functions
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
            'n_estimators =',       str( model.n_estimators ).      ljust( 10 ),
            'learning_rate =',      str( model.learning_rate ).     ljust( 10 ),
            'max_depth =',          str( model.max_depth )         
            )
    print   (
            'min_samples_leaf =',   str( model.min_samples_leaf ).  ljust( 10 ),
            'max_features  =',      str( model.max_features ).      ljust( 10 ),
            'loss      =',          str( model.loss )                
            )
    print   ( 'value for analysis = ', value_to_predict )
    print_line_of_dashes()

    # sys.stdout = old_stdout
    # print_log ( log_file, log_file_name )

def results_model_performance ( model, single_country_df, y_train, y_test, X_train, X_test, value_to_predict ): 
    # log_file_name = '2_model_performance'
    # old_stdout, log_file = log_screen_print_statements( log_file_name, sys.stdout )

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
    # log_file_name = '3_important_feature'
    # old_stdout, log_file = log_screen_print_statements( log_file_name, sys.stdout )

    print_line_of_dashes()
    print ( 'Feature Importance (descending order) - relative to overall importance' )
    print_line_of_dashes()

    importance = model.feature_importances_
    feature_indexes_by_importance = importance.argsort()
    for index in reversed( feature_indexes_by_importance ):
        importance_percent = str ( round( ( importance[index] * 100.0 ), 2 ) ) + ' %' 
        print (   str( feature_labels[index] ).ljust( 30 ), importance_percent)
    print_line_of_dashes()   

    # sys.stdout = old_stdout
    # print_log ( log_file, log_file_name )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Working Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def feature_list( share_df ):
    function_start_time = time.time()
    log_process_commencing  ( 'determine list of share features' )

    column_name_list_from_share_df = list(share_df.columns.values)
    features = []
    invalid_ml_columns = []

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
            features.append(column)
        else:
            invalid_ml_columns.append(column)

    feature_labels = np.array( features )

    log_df_process_completed( share_df, function_start_time )
    return ( features, invalid_ml_columns, feature_labels )

def create_df_with_features_only ( share_df, features ):
    function_start_time = time.time()
    log_process_commencing  ( 'subsetting features dataframe share_df' )

    features_df = share_df[features].copy()

    log_df_process_completed( share_df, function_start_time )
    return ( features_df )

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





def machine_learning_manager( share_df ):
    core_process_name           = 'Generate Machine Learning Model'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    features, invalid_ml_columns, feature_labels = feature_list( share_df)

    print ( '' )
    print ( features )
    print ( '' )
    print ( feature_labels )
    print ( '' )
    print ( invalid_ml_columns )


    features_only_df = create_df_with_features_only( share_df, features )

    gradient_boosting_regressor( features_only_df, share_df, feature_labels, 'close' )
    # ordinary_least_squares_regression ( core_df, value_to_predict, features )

    log_core_process_footer( core_process_name, core_process_start_time )


