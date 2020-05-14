### Data sources

In order to validate the claims from [this](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) article, I pulled data from the FRED database, which pulls from the BLS. Each link will take you to the exact series that I downloaded here.

- [CPI (for inflation)](https://fred.stlouisfed.org/series/CPIAUCSL)
- [Poultry](https://fred.stlouisfed.org/series/APU0000706111)
- [Pork](https://fred.stlouisfed.org/series/APU0000FD3101)
- [Beef](https://fred.stlouisfed.org/series/APU0000703112)

The data from the FRED does NOT go back to 1935.


![png](price_check_files/price_check_1_0.png)


Quotes taken directly from the article

> 1. "poultry costs U.S. consumers 62% less in inflation-adjusted terms than it did in 1935"

> 2. "Pork, now also raised mostly at factory scale indoors, is 12% cheaper"

> 3. "Beef, which isn’t, costs 63% more."

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


### Limitations

- Maybe I deflated prices using a different CPI than the author
- My numbers certainly aren't in the same date range?
