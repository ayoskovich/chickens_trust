### Data sources

In order to validate the claims from [this](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) article, I pulled price data from FRED (which sources data from the BLS) and adjusted it using the CPI. Data sources are here:

- [CPI (for inflation)](https://fred.stlouisfed.org/series/CPIAUCSL)
- [Poultry](https://fred.stlouisfed.org/series/APU0000706111)
- [Pork](https://fred.stlouisfed.org/series/APU0000FD3101)
- [Beef](https://fred.stlouisfed.org/series/APU0000703112)

**A note here**: I couldn't for the life of me, find any data that goes back to 1935, like Fox cites in the article. The earliest history I could find from FRED or the BLS only goes back to the 80s, so I must be missing something!


![png](price_check_files/price_check_1_0.png)


Now I'll simply take the percentage difference between the oldest and most recent price.

    chicken
    	Oldest: 1980-01-01 00:00:00
    	Newest: 2020-04-01 00:00:00
    	$2.29 --> $1.57
    	pct change: -0.315
    pork
    	Oldest: 1998-01-01 00:00:00
    	Newest: 2020-04-01 00:00:00
    	$5.01 --> $3.67
    	pct change: -0.267
    beef
    	Oldest: 1984-01-01 00:00:00
    	Newest: 2020-04-01 00:00:00
    	$3.23 --> $4.05
    	pct change: 0.253


Quotes taken directly from the article

> 1. "poultry costs U.S. consumers 62% less in inflation-adjusted terms than it did in 1935"
    - From 1980 - 2020, chicken prices have declined 31.5%.

> 2. "Pork, now also raised mostly at factory scale indoors, is 12% cheaper"
    - From 1998 - 2020, the price of pork has declined 26%.

> 3. "Beef, which isn’t, costs 63% more."
    - From 1984 - 2020, the price of beef has increased 25.3%.

### Limitations

- Maybe I deflated prices using a different CPI than the author
- My numbers certainly aren't in the same date range?
