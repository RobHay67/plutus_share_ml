# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# External Modules
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import time                             # for reporting how much time the functions take to finish
import datetime                         # use for setting the end of campaign date
# ....x....1....x....2....x....3....x....4....x....5....x....6....x....7....x....8....x....9....x....0....x....1....x....2....x....3....x....4....x....5....x....6....x....7
tab1, tab2, tab3, tab4, tab5, tab6 = 63, 12, 35, 10, 10, 17
tab_to_end  = tab1 + tab2 + tab3 + tab4 
line_length = tab1 + tab2 + tab3 + tab4 + tab5
# ljust lengthens the printed word to the specified number of spaces - so 'word'.ljust(5) results in 'word ' with the extra space at the end.
col_headings = str      ( 
                        'process'.                  ljust(tab1) + 
                        'progress'.                 ljust(tab2) + 
                        'rows'.                     ljust(tab3) + 
                        'columns'.                  ljust(tab4) +
                        'load time'.                ljust(tab5)      
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
    print_line_of_equals()

def log_application_footer( start_time ):
    current_time = time.time()
    time_difference_seconds = round( ( ( current_time - start_time )      ), 2 ) 
    time_difference_minutes = round( ( ( current_time - start_time ) / 60 ), 2 ) 
    print_line_of_equals()
    print(      'FINISHED PROCESSING @', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '- total load time =', time_difference_seconds, 'seconds  - ', time_difference_minutes, 'minutes' )
    print_line_of_equals()



def log_process_commencing( sub_process ):
    print( str(sub_process ).ljust( 50 ), end ='')


def log_process_completed( no_of_rows, no_of_columns, start_time, result='Completed', error_message=None):
    current_time = time.time()
    diff = str ( round( ( current_time - start_time ), 3 ) )
    time_difference = ( '.'.join(map('{0:0>3}'.format, diff.split('.'))) )  
    if error_message is not None : result =  '-FAILURE-'
    print( result.ljust( tab2 - 1),  str(no_of_rows).ljust( tab3 - 1 ),  str(no_of_columns).ljust( tab4 - 1 ), 'seconds = ' + str ( time_difference ) )
    if error_message is not None : print ( error_message )


