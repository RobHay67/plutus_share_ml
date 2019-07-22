# --------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# Primary Machine Learning Code
#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------





# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Working Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def feature_list( core_df, core_df_name ):
    function_start_time = time.time()
    log_process_commencing  ( 'determine list of features', core_df_name )

    column_name_list_from_core_df = list(core_df.columns.values)
    features = []
    invalid_ml_columns = []

    for column in column_name_list_from_core_df:
        boolean_status = 'unknown'
        column_to_assess = core_df[column].value_counts().to_frame().reset_index()
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

    log_process_completed  ( 0, 0, 1, len( features ), function_start_time )
    return ( features, invalid_ml_columns )





