## Data sources

In order to validate the claims from [this](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) article, I pulled price data from FRED (which sources data from the BLS) and adjusted it using the CPI. Data sources are here:

- [Poultry](https://fred.stlouisfed.org/series/APU0000706111)
- [Pork](https://fred.stlouisfed.org/series/APU0000FD3101)
- [Beef](https://fred.stlouisfed.org/series/APU0000703112)

poultry -.62
pork -.12
beef +.63

The chart below shows how the average price of 3 different types of meats has changed over time. However, these are nominal dollars, not real dollars. To adjust for the change in purchasing power of a dollar, I'll use the CPI to adjust the prices.

    /opt/anaconda3/lib/python3.7/site-packages/statsmodels/tools/_testing.py:19: FutureWarning: pandas.util.testing is deprecated. Use the functions in the public API at pandas.testing instead.
      import pandas.util.testing as tm



![png](price_check_files/price_check_3_1.png)



![png](price_check_files/price_check_4_0.png)


A couple things to note here.

- Pork has certainly declined in real price
- Beef has increased in real price
- Chicken, while the nominal price has increased, the increase in dollar purchasing power outweighed that change, so chicken is less expensive than it was in the 80s.

I'll translate these results into % changes, simply by taking the pct change between the min and max dates and keep track of the start / end dates.




<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Meat</th>
      <th>Change</th>
      <th>Start</th>
      <th>End</th>
      <th>NumYears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Beef</td>
      <td>0.253233</td>
      <td>1984-01-01</td>
      <td>2020-04-01</td>
      <td>36</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Chicken</td>
      <td>-0.314954</td>
      <td>1980-01-01</td>
      <td>2020-04-01</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Pork</td>
      <td>-0.266726</td>
      <td>1998-01-01</td>
      <td>2020-04-01</td>
      <td>22</td>
    </tr>
  </tbody>
</table>



The author of the article used different date ranges than I did, he found data that goes back to 1935, with is 85 years in total. I'll make a massive assumption that the price change has been consistent over each year, and I'll extrapolate backwards.




<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Meat</th>
      <th>Change</th>
      <th>Start</th>
      <th>End</th>
      <th>NumYears</th>
      <th>Extrap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Beef</td>
      <td>0.253233</td>
      <td>1984-01-01</td>
      <td>2020-04-01</td>
      <td>36</td>
      <td>0.597911</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Chicken</td>
      <td>-0.314954</td>
      <td>1980-01-01</td>
      <td>2020-04-01</td>
      <td>40</td>
      <td>-0.669277</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Pork</td>
      <td>-0.266726</td>
      <td>1998-01-01</td>
      <td>2020-04-01</td>
      <td>22</td>
      <td>-1.030534</td>
    </tr>
  </tbody>
</table>


