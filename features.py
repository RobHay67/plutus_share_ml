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


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Machine Learning Feature Management
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def remove_minimal_impact_features( features, share_df ):
    function_start_time = time.time()
    log_process_commencing  ( 'determine list of share features' )

    import_features =   {
                        'counter_min'               : '0 impact', 
                        }
    
    date_features =     { 
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
    price_features =    {                       
                        }

    volume_features =   { 
                        }

    features_with_minimal_impact = { **import_features, **date_features, **price_features, **volume_features }

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
# Prediction Features
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def close_higher_in_future( share_df ):
    # future_close_01 < close
    function_start_time = time.time()
    log_process_commencing( str( 'determine if price is higher tomorrow' )  )

    share_df['Y_close'] = np.where( share_df['future_close_01'] > share_df['close'], 1, 0)   

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

    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_df )   

