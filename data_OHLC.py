# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import pathlib                      # for handling local dorectories
import time                         # for reporting how much time the functions take to finish
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Local Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from application_log                import log_core_process_header, log_core_process_footer
from application_log                import log_process_commencing,  log_df_process_completed


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# File Locations and module information
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
ohlc_share_df_folder    = pathlib.Path.home().joinpath('shares', 'ohlc', )
ohlc_share_df_filename  = pathlib.Path.joinpath(ohlc_share_df_folder, 'test_ohlc_shares.csv' )
# ohlc_share_df_filename  = pathlib.Path.joinpath(ohlc_share_df_folder, 'entire_ohlc_shares.csv' )

share_df_dict =     {
                    'share_code'    :'object',
                    # 'trading_date'  :'date',   # this field is loaded using the parse_dates param - so do not specify in col list 
                    'open'          :'float64',
                    'high'          :'float64', 
                    'low'           :'float64', 
                    'close'         :'float64', 
                    'volume'        :'float64',
                    'date'          :'object'              
                    }

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helper Functions
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def list_of_share_codes( share_df ):
#     # share_df.reset_index( inplace=True )
#     return ( share_df.share_code.unique().tolist() )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Workers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def load_OHLC_share_df():
    function_start_time = time.time()
    log_process_commencing( str( 'loading OHLC' )  )

    share_df = pd.read_csv( ohlc_share_df_filename, dtype=share_df_dict, parse_dates=['trading_date'] )

    log_df_process_completed( share_df, function_start_time )

    print ( 'first date        in share file = ', share_df.trading_date.min() )         # print some additional information
    print ( 'last  date        in share file = ', share_df.trading_date.max() )
    
    return ( share_df )   

def save_ohlc_share_df( share_df) :
    core_process_name           = 'SAVE OHLC Share data'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    function_start_time = time.time()
    log_process_commencing( str( 'saving OHLC' )  )

    share_df.reset_index( inplace=True )
    share_df.to_csv( ohlc_share_df_filename, index=False )

    log_df_process_completed( share_df, function_start_time )
    log_core_process_footer( core_process_name, core_process_start_time )

def add_sequential_counter( share_df ):
    function_start_time = time.time()
    log_process_commencing( str( 'add sequential counter to OHLC share data' ) )

    share_df['counter']     = share_df.groupby(['share_code']).cumcount()+1
    share_df['counter_min'] = share_df.groupby( 'share_code')['counter'].transform('min')
    share_df['counter_max'] = share_df.groupby( 'share_code')['counter'].transform('max')

    log_df_process_completed( share_df, function_start_time )
    return ( share_df )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Manager Function
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def load_ohlc_data_file():
    core_process_name           = 'Load OHLC Share data'
    core_process_start_time     = time.time()
    log_core_process_header     (  core_process_name )

    share_df    = load_OHLC_share_df()

    share_df    = add_sequential_counter( share_df ) 
   
    log_core_process_footer( core_process_name, core_process_start_time )
    return ( share_df )   





