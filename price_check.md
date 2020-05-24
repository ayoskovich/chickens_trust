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


A couple things to note here:

- Pork has certainly declined in real price
- Beef has increased in real price
- Chicken, while the nominal price has increased, the increase in dollar purchasing power outweighed that change, so chicken is less expensive than it was in the 80s.

I'll translate these results into % changes, simply by taking the pct change between the min and max dates and keep track of the start / end dates. I'll also adjust for the differing number of years between me and the author.




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
      <th>price</th>
      <th>Series</th>
      <th>date</th>
      <th>Meat</th>
      <th>cpi</th>
      <th>cur_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.290</td>
      <td>APU0000703112</td>
      <td>1984-01-01</td>
      <td>Beef</td>
      <td>102.100</td>
      <td>3.233238</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.340</td>
      <td>APU0000703112</td>
      <td>1984-02-01</td>
      <td>Beef</td>
      <td>102.600</td>
      <td>3.342190</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.308</td>
      <td>APU0000703112</td>
      <td>1984-03-01</td>
      <td>Beef</td>
      <td>102.900</td>
      <td>3.252865</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.331</td>
      <td>APU0000703112</td>
      <td>1984-04-01</td>
      <td>Beef</td>
      <td>103.300</td>
      <td>3.297246</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.301</td>
      <td>APU0000703112</td>
      <td>1984-05-01</td>
      <td>Beef</td>
      <td>103.500</td>
      <td>3.216701</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1183</th>
      <td>3.391</td>
      <td>APU0000FD3101</td>
      <td>2019-12-01</td>
      <td>Pork</td>
      <td>258.444</td>
      <td>3.357647</td>
    </tr>
    <tr>
      <th>1184</th>
      <td>3.368</td>
      <td>APU0000FD3101</td>
      <td>2020-01-01</td>
      <td>Pork</td>
      <td>258.820</td>
      <td>3.330028</td>
    </tr>
    <tr>
      <th>1185</th>
      <td>3.419</td>
      <td>APU0000FD3101</td>
      <td>2020-02-01</td>
      <td>Pork</td>
      <td>259.050</td>
      <td>3.377452</td>
    </tr>
    <tr>
      <th>1186</th>
      <td>3.415</td>
      <td>APU0000FD3101</td>
      <td>2020-03-01</td>
      <td>Pork</td>
      <td>257.953</td>
      <td>3.387847</td>
    </tr>
    <tr>
      <th>1187</th>
      <td>3.673</td>
      <td>APU0000FD3101</td>
      <td>2020-04-01</td>
      <td>Pork</td>
      <td>255.902</td>
      <td>3.673000</td>
    </tr>
  </tbody>
</table>
<p>1188 rows × 6 columns</p>
</div>



Now that I've extrapolated the changes, let's compare the numbers I got to Fox's original numbers.


![png](price_check_files/price_check_9_0.png)

