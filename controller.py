import pandas as pd

import app
import dates
import price
import volume

pd.set_option('display.max_columns', None)

# ----------------------------------------------- load the OHLC share data from Disk
share_df = app.load_OHLC_share_df()
list_of_share_codes = app.list_of_share_codes( share_df )
# ----------------------------------------------- Add a counter for the code to reference
share_df = app.add_sequential_counter( share_df )

# ----------------------------------------------- Attach Volume Features to the dataset
share_df = volume.add_average_volume( share_df )
share_df = volume.volume_values( share_df )
# ----------------------------------------------- Attach Price  Features to the dataset
share_df = price.price_values( share_df )




# ----------------------------------------------- Attach Date Features to the dataset
share_df = dates.add_day_of_the_week_features( share_df )
share_df = dates.add_month_of_the_year_features( share_df )

print ( share_df.tail(7) )


# ----------------------------------------------- Save the OHLC Share Dataframe to Disk
# app.save_OHLC_share_df( share_df )


