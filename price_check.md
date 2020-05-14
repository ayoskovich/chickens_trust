### Data sources

In order to validate the claims from [this](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) article, I pulled data from the FRED database, which pulls from the BLS. Each link will take you to the exact series that I downloaded here.

- [CPI (for inflation)](https://fred.stlouisfed.org/series/CPIAUCSL)
- [Poultry](https://fred.stlouisfed.org/series/APU0000706111)
- [Pork](https://fred.stlouisfed.org/series/APU0000FD3101)
- [Beef](https://fred.stlouisfed.org/series/APU0000703112)

The data from the fred does NOT go back to 1935, I'm not 100% sure where that historic data is coming from...


![png](price_check_files/price_check_1_0.png)


Quotes taken directly from the article

> 1. "poultry costs U.S. consumers 62% less in inflation-adjusted terms than it did in 1935"

> 2. "Pork, now also raised mostly at factory scale indoors, is 12% cheaper"

> 3. "Beef, which isn’t, costs 63% more."

    chicken:
      $2.29 --> $1.57: -0.31
    pork:
      $5.01 --> $3.67: -0.27
    beef:
      $3.23 --> $4.05: 0.25

