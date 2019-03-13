import pandas as pd

import app



# ----------------------------------------------- load the OHLC share data from Disk
share_df = app.load_OHLC_share_df()

# list_of_share_codes = app.list_of_share_codes( share_df )

# ----------------------------------------------- Add a counter for the code to reference
share_df = app.add_sequential_counter( share_df )

# ----------------------------------------------- Attach Features to the dataset
share_df = app.add_day_of_the_week_features( share_df )
share_df = app.add_month_of_the_year_features( share_df )


# subset the test data to be 2 share codes so we can test the sequence
# add the sequence first
# work on the price indicators because then we can set up the machine learning and the the P score for the data





# ----------------------------------------------- Save the OHLC Share Dataframe to Disk
app.save_OHLC_share_df( share_df )


# print ( share_df.feat_date_is_mon.value_counts() )
print ( share_df.head(100) )
