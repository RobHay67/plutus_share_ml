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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing, log_df_process_completed




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




def build_machine_learning_model( share_df ):
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


    # features_only_df = create_df_with_features_only( core_df, core_df_name, features )
    # mo_value_for_analysis = value_for_analysis.replace('lcl', 'aud')

    # gradient_boosting_regressor( features_only_df, core_df, feature_labels, mo_value_for_analysis )
    # ordinary_least_squares_regression ( core_df, mo_value_for_analysis, features )

    log_core_process_footer( core_process_name, core_process_start_time )


