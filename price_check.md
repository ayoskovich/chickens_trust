## Data sources

In order to validate the claims from [this](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) article, I pulled price data from FRED (which sources data from the BLS) and adjusted it using the CPI. Data sources are here:

- [Data finder](https://beta.bls.gov/dataQuery/find?st=0&r=20&s=popularity%3AD&more=0)
- [CPI (for inflation)](https://fred.stlouisfed.org/series/CPIAUCSL)
- [Poultry](https://fred.stlouisfed.org/series/APU0000706111)
- [Pork](https://fred.stlouisfed.org/series/APU0000FD3101)
- [Beef](https://fred.stlouisfed.org/series/APU0000703112)




    -0.6186046511627907




![png](price_check_files/price_check_2_0.png)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Series ID</th>
      <th>Year</th>
      <th>Period</th>
      <th>Label</th>
      <th>Value</th>
      <th>Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CUUR0000SEFF</td>
      <td>1935</td>
      <td>M01</td>
      <td>1935 Jan</td>
      <td>32.4</td>
      <td>1935-01-01</td>
    </tr>
    <tr>
      <th>0</th>
      <td>CUUR0000SEFD</td>
      <td>1935</td>
      <td>M01</td>
      <td>1935 Jan</td>
      <td>13.0</td>
      <td>1935-01-01</td>
    </tr>
    <tr>
      <th>0</th>
      <td>CUUR0000SEFC</td>
      <td>1935</td>
      <td>M01</td>
      <td>1935 Jan</td>
      <td>10.2</td>
      <td>1935-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CUUR0000SEFF</td>
      <td>1935</td>
      <td>M02</td>
      <td>1935 Feb</td>
      <td>34.5</td>
      <td>1935-02-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CUUR0000SEFD</td>
      <td>1935</td>
      <td>M02</td>
      <td>1935 Feb</td>
      <td>13.3</td>
      <td>1935-02-01</td>
    </tr>
  </tbody>
</table>
</div>




![png](price_check_files/price_check_4_0.png)


## Claims

> "poultry costs U.S. consumers 62% less in inflation-adjusted terms than it did in 1935"

> "Pork, now also raised mostly at factory scale indoors, is 12% cheaper"

> "Beef, which isn’t, costs 63% more."

Here's what I found:

- From 1980 - 2020, chicken prices have declined 31.5%.
- From 1998 - 2020, the price of pork has declined 26%.
- From 1984 - 2020, the price of beef has increased 25.3%.

But it wouldn't be fair to compare these numbers to his numbers, because my data has a different number of years. I'll very simply extrapolate backwards using the growth rate I have from my data.




<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Type</th>
      <th>My pct change</th>
      <th>His pct change</th>
      <th>My Years</th>
      <th>His years</th>
      <th>My extrapolated change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chicken</td>
      <td>-0.31</td>
      <td>-0.62</td>
      <td>40</td>
      <td>85</td>
      <td>-0.67</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pork</td>
      <td>-0.27</td>
      <td>-0.12</td>
      <td>22</td>
      <td>85</td>
      <td>-1.03</td>
    </tr>
    <tr>
      <th>2</th>
      <td>beef</td>
      <td>0.25</td>
      <td>0.63</td>
      <td>36</td>
      <td>85</td>
      <td>0.60</td>
    </tr>
  </tbody>
</table>



Now I can look at how far off I was (mine - his).




<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Type</th>
      <th>error</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chicken</td>
      <td>-0.05</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pork</td>
      <td>-0.91</td>
    </tr>
    <tr>
      <th>2</th>
      <td>beef</td>
      <td>-0.03</td>
    </tr>
  </tbody>
</table>


