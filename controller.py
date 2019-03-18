import pandas as pd

import app
import dates
import price

pd.set_option('display.max_columns', None)

# ----------------------------------------------- load the OHLC share data from Disk
share_df = app.load_OHLC_share_df()
list_of_share_codes = app.list_of_share_codes( share_df )
# print ( share_df.head(3) )

# ----------------------------------------------- Add a counter for the code to reference
share_df = app.add_sequential_counter( share_df )
# print ( share_df.head(4) )
# ----------------------------------------------- Attach Date Features to the dataset
# share_df = dates.add_day_of_the_week_features( share_df )
# share_df = dates.add_month_of_the_year_features( share_df )

# ----------------------------------------------- Attache Price Features to the dataset
share_df = price.past_share_prices( share_df )
print ( share_df.tail(7) )



# work on the price indicators because then we can set up the machine learning and the the P score for the data

# print ( share_df.sample(3) )

# ----------------------------------------------- Save the OHLC Share Dataframe to Disk
# app.save_OHLC_share_df( share_df )


# print ( share_df.feat_date_is_mon.value_counts() )
# print ( share_df.head(10) )
