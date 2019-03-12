# This is going to be python code

# general process - load up the OHLC dataset and add features to IT

# Definition of features.........


# Period Identifyer
    Need to generate a sequential period number
    We may need a date filler routine as well? not sure about This


# Basic Share identifiers and Info
    Industry
    Dividend_Cum_Date
    Dividend_annoncement_Date
    Dividend_amount
    Dividend_yield
    Franking Credits amount and is it even offered


# Time of the Year
#   feat_day_mon
    feat_day_tue
    day of the month
    month
    Public holidays



# Price Indicators
    Differential from yesterday
    Differential from 2 days ago
    Price in 1 days time
    Price in 2 days time
    Price in 5 days time
    price in 30 days time   etc
    perhaps these should be represented as a percentage and then categorised accordingly

# Price Direction Indicators
    Price going up (and then how many days - ie last2, 3, 4, 5 days etc)
    price going down
    Price has not changed
    gaps between prior close and current open
        Probaly % size of the gap for relativity
    


# Volume Indicators
    Averge Vol today
    Averge Vol yesterday
    Avg Vol for last 2 days, last 5 days, last 10 days etc
    Vol into the future by an appropriate amount 1 day, 2 days, 5, 10 ,30 days
    Is the above just the moving average - 
    < check how the MACD works to smooth out the averages > migth be over sampling here?


# EXTERNAL INFORMATION
    Interest Rates
    Bond Rates
    Gold Price
    Key Commodity Prices
        Gold
        Coppers
        rare earths
        Iron...
        Average Labour Rates
    Company tax rates (average)








