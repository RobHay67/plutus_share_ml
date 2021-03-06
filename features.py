# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import time                         # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_df_process_completed
from common                         import closing_price_column_name, past_and_future_periods, column_name_close_future, column_name_price_higher
from common                         import average_volume_per_minute_column_name, moving_average_periods, column_name_volume_ma_higher, column_name_volume_moving_average


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Machine Learning Feature Management
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def remove_minimal_impact_features( features, share_df ):
    function_start_time = time.time()
    log_process_commencing  ( 'determine list of share features' )

    prediction_features =   {
                            closing_price_column_name   : 'primary prediction value'
                            }
    for column in share_df:
        if column[:2] == 'Y_':                                                  # add any columns with a Y prefix as these are potentially things we want to try and predict
            prediction_features.update( { column : 'Prediction Variable'} )

    import_features =       {
                            'counter_min'               : '0 impact', 
                            }
    
    date_features =         { 
                            'feat_date_is_sun'          : '0 impact', 
                            'feat_date_is_sat'          : '0 impact', 
                            'feat_date_is_nov'          : '< 5% impact', 
                            'feat_date_is_mar'          : '< 5% impact', 
                            'feat_date_is_dec'          : '< 5% impact', 
                            'feat_date_is_fri'          : '< 5% impact', 
                            'feat_date_is_oct'          : '< 5% impact', 
                            'feat_date_is_jun'          : '< 5% impact', 
                            'feat_date_is_thur'         : '< 5% impact', 
                            'feat_date_is_feb'          : '< 5% impact', 
                            'feat_date_is_apr'          : '< 5% impact', 
                            }
    price_features =        {                       
                            }

    volume_features =       { 
                            }

    features_with_minimal_impact = { **prediction_features,  **import_features, **date_features, **price_features, **volume_features }

    for feature in features_with_minimal_impact.keys():
        if feature in features:
            features.remove( feature )
    
    log_df_process_completed( share_df, function_start_time )
    return ( features )

def remove_multi_collinearity_features( features, share_df ):
    function_start_time = time.time()  
    log_process_commencing  ( 'remove multi collinearity features' )

    multi_collinearity_list     =   { 
                                    }

    for feature in multi_collinearity_list.keys():
        if feature in features:
            features.remove( feature )   
    
    log_df_process_completed( share_df, function_start_time )
    return ( features )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Assessment Features
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def volume_above_ma_per_minute( share_df ):
    function_start_time = time.time()
    log_process_commencing( str( 'determine if volume is above moving averages' )  )

    for period_no in moving_average_periods: 
        new_moving_average_col, new_moving_average_per_minute_col  = column_name_volume_moving_average( period_no )
        # print ( new_moving_average_per_minute_col )
        volume_ma_higher_column_name = column_name_volume_ma_higher( period_no )
        share_df[ volume_ma_higher_column_name ] = np.where( share_df[ average_volume_per_minute_column_name ] > share_df[ new_moving_average_per_minute_col ], 1, 0)   

    log_df_process_completed( share_df, function_start_time )       
    return ( share_df )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Prediction Features
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def close_higher_in_future( share_df ):
    function_start_time = time.time()
    log_process_commencing( str( 'determine if price is higher tomorrow' )  )

    for period_no in past_and_future_periods:       
        future_close_column      = column_name_close_future( period_no )
        close_higher_column_name = column_name_price_higher( period_no )
        share_df[ close_higher_column_name ] = np.where( share_df[ future_close_column ] > share_df[ closing_price_column_name ], 1, 0)   

    log_df_process_completed( share_df, function_start_time )       
    return ( share_df )




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Feature Manager
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def add_primary_analysis_features( share_df ):
    core_process_name           = 'Add Analysis Features'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    
    share_df            = close_higher_in_future( share_df )
    share_df            = volume_above_ma_per_minute( share_df )

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_df )   

