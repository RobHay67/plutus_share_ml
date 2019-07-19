# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import time                             # for reporting how much time the functions take to finish
import datetime                         # use for setting the end of campaign date
import sys                              # Show version of Python which is currently running
# ....x....1....x....2....x....3....x....4....x....5....x....6....x....7....x....8....x....9....x....0....x....1....x....2....x....3....x....4....x....5....x....6....x....7
tab1, tab2, tab3, tab4, tab5, tab6 = 70, 15, 15, 10, 10, 20
tab_to_end  = tab1 + tab2 + tab3 + tab4 + tab5
line_length = tab1 + tab2 + tab3 + tab4 + tab5 + tab6
# ljust lengthens the printed word to the specified number of spaces - so 'word'.ljust(5) results in 'word ' with the extra space at the end.
col_headings = str      ( 
                        'process'.                  ljust(tab1) + 
                        'progress'.                 ljust(tab2) + 
                        'share codes'.              ljust(tab3) + 
                        'rows'.                     ljust(tab4) + 
                        'columns'.                  ljust(tab5) +
                        'load time'.                ljust(tab6)      
                        )



def print_seperator( seperator_type ):
    if   seperator_type=='key'      : print ( '=' * line_length )
    elif seperator_type == 'single' : print ( '-' * line_length )
    else                            : print ( '*' * line_length )

def print_line_of_dashes(): print('-'*line_length)
def print_line_of_equals(): print('='*line_length)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Application header and footer
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def log_application_header():
    print ('\n' * 20)  
    print_line_of_equals()
    print ( '\n' )
    print('PLUTUS Share Data Anayser and Machine Learning code base - '.upper(), ' - commenced @',  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') )
    print ( '\n' )
    print ( sys.version )
    print ( sys.executable )   
    print ( '\n' )        
    print_line_of_equals()

def log_application_footer( start_time ):
    current_time = time.time()
    time_difference_seconds = round( ( ( current_time - start_time )      ), 2 ) 
    time_difference_minutes = round( ( ( current_time - start_time ) / 60 ), 2 ) 
    print_line_of_equals()
    print(      'FINISHED PROCESSING @', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '- total processing time =', time_difference_seconds, 'seconds  - ', time_difference_minutes, 'minutes' )
    print_line_of_equals()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Core Process Section Header and Footer - used for Load Tables, Merge Tables, Add Features
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def log_core_process_header( core_process ):
    print_line_of_dashes()
    print ( core_process )
    print ( col_headings )
    print_line_of_dashes()

def log_core_process_footer( core_process, start_time):
    current_time = time.time()
    time_difference_seconds = str ( round( ( current_time - start_time ), 3 ) )
    time_difference_seconds = ( '.'.join(map('{0:0>2}'.format, time_difference_seconds.split('.'))) )   
    time_difference_minutes = str ( round( ( ( current_time - start_time ) / 60 ), 3 ) )
    time_difference_minutes = ( '.'.join(map('{0:0>3}'.format, time_difference_minutes.split('.'))) )   
    print_line_of_dashes()
    print       (      
                # core_process.                                   ljust( tab1 - 1        ), 
                ''.                                   ljust( tab1 - 1        ), 
                str( 'COMPLETED' ).                             ljust( tab2 - 1        ), 
                str( 'total time =').                           ljust( tab3 - 1        ), 
                str( time_difference_seconds + ' seconds' ).    ljust( tab4 + tab5 - 4 ), 
                str( time_difference_minutes + ' minutes' ) 
                )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sub Process - specific process currently being undertaken
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def log_process_commencing( sub_process ):
    print( str(sub_process ).ljust( tab1 ), end ='')

def log_dict_process_completed( share_dict, start_time, result='Completed', error_message=None):
    no_of_share_codes   = len( share_dict )
    no_of_rows          = 0
    no_of_columns       = 0
    for share_data in share_dict.values():   
        no_of_rows          += len( share_data )
        no_of_columns       += len( share_data.columns )
    no_of_columns   = no_of_columns / no_of_share_codes

    current_time = time.time()
    diff = str ( round( ( current_time - start_time ), 3 ) )
    time_difference = ( '.'.join(map('{0:0>3}'.format, diff.split('.'))) )  
    if error_message is not None : result =  '-FAILURE-'
    print(  result.                     ljust( tab2 - 1), 
            str( no_of_share_codes ).   ljust( tab3 - 1 ), 
            str( no_of_rows ).          ljust( tab4 - 1 ),  
            str( no_of_columns ).       ljust( tab5 - 1 ), 
            'seconds = ' + str ( time_difference ) )
    if error_message is not None : print ( error_message )


def log_df_process_completed( share_df, start_time, result='Completed', error_message=None):
    no_of_share_codes   = len( share_df.share_code.unique().tolist() )   
    no_of_rows          = len( share_df )
    no_of_columns       = len( share_df.columns )

    current_time = time.time()
    diff = str ( round( ( current_time - start_time ), 3 ) )
    time_difference = ( '.'.join(map('{0:0>3}'.format, diff.split('.'))) )  
    if error_message is not None : result =  '-FAILURE-'
    print(  result.                     ljust( tab2 - 1), 
            str( no_of_share_codes ).   ljust( tab3 - 1 ), 
            str( no_of_rows ).          ljust( tab4 - 1 ),  
            str( no_of_columns ).       ljust( tab5 - 1 ), 
            'seconds = ' + str ( time_difference ) )
    if error_message is not None : print ( error_message )
