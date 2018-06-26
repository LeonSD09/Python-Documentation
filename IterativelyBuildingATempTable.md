
# Iteratively Building a Teradata Temp Table w/ Python

#### IMPORTANT NOTE ####
_As this particular documentation was written with my colleagues at work, and I work at Apple, and Apple is very much about privacy, references to potentially sensitive information have been omitted_ 😎

I was trying to run a query in Teradata (TD) over a given date range but it kept timing out on me. My solution to this problem was to build a temp table and load the data I needed in chunks. Unfortunately, both my query and the INSERT statement I was using to load the table only worked on one day at a time. 😓

I wrote a quick Python script that iterates over a given date range and builds out my temp table one day at time. I put a 12 day date range in, kicked off the query, and watched it build out my table while I ate lunch. This was WAY better than running the INSERT statement, changing the date, repeating until I had all my data. Here's how I did it:

Here are the Python packages needed to make this happen:

```
from datetime import date, timedelta
import pandas as pd
import aos_td
import time
```

Pandas has a nifty function that you can give a start and end date to and it will generate the range for you. I used it to just sequentially build out 4 consecutive days but it can do [some other pretty cool things](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#generating-ranges-of-timestamps). The last line in the block below is a fancy *list comprehension* that just takes the Pandas object it creates and converts it into a list that I can iterate through, putting the dates in the YYYY-MM-DD format that TD likes.

```
start = date(2016,8,17)
end = date(2016,8,20)
dts = [d.strftime('%Y-%m-%d') for d in pd.date_range(start, end)]
```

The query is held in a string with a parameter *$[dt] *used in the date filter. This value will be replaced when the query is actually run in the next block of code.

``` sql
query = """
<SENSITIVE INFORMATION OMITTED>
"""
```

Finally, I iterated through the dates in my date list (*dts*), building my INSERT statement with the correct date and loading the data into my temp table. I added a little status message just so I can monitor the progress as I ate lunch. I also through in some timing code (*s1/e1/s2/e2...*) just for profiling the speed of the script and query.

``` python
s1 = time.time()
for dt in dts:

    s2 = time.time()

    with aos_td.default_session() as session:
        aos_td.query(session, query.replace('$[dt]',"'" + dt + "'")).next()
    
    e2 = time.time()

    print 'Inserted: ' + dt + "\t\t Time Elapsed: " + str(round(e2 - s2, 1)) + 's'

e1 = time.time()
print '-----------------------------------------------------'
print "Total Time Elapsed: " + str(round(e1 - s1, 1)) + 's'
```

Below is what my terminal window looked like as it worked for me:

```
Inserted: 2016-08-17         Time Elapsed: 125.7s
Inserted: 2016-08-18         Time Elapsed: 138.6s
Inserted: 2016-08-19         Time Elapsed: 148.8s
Inserted: 2016-08-20         Time Elapsed: 139.7s
-----------------------------------------------------
Total Time Elapsed: 552.8s
```

Almost 10 minutes to build out four days - probably faster than I could have done it manually. 🤓
