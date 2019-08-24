# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import time                         # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_process_commencing, log_df_process_completed



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Feature Managemenbt
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