## Data sources

In order to validate the claims from [this](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P) article, I pulled price data from FRED (which sources data from the BLS) and adjusted it using the CPI. Data sources are here:

- Poultry 
    - [price](https://fred.stlouisfed.org/series/APU0000706111)
    - [index](https://beta.bls.gov/dataViewer/view/timeseries/CUUR0000SEFF)
- Pork
    - [price](https://fred.stlouisfed.org/series/APU0000FD3101)
    - [index](https://beta.bls.gov/dataViewer/view/timeseries/CUUR0000SEFD)
- Beef
    - [price](https://fred.stlouisfed.org/series/APU0000703112)
    - [index](https://beta.bls.gov/dataViewer/view/timeseries/CUUR0000SEFC)


![png](price_check_files/price_check_1_0.png)



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
      <th>DATE</th>
      <th>price</th>
      <th>Series</th>
      <th>Date</th>
      <th>Meat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1998-01-01</td>
      <td>3.171</td>
      <td>APU0000FD3101</td>
      <td>1998-01-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1998-02-01</td>
      <td>3.134</td>
      <td>APU0000FD3101</td>
      <td>1998-02-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1998-03-01</td>
      <td>3.032</td>
      <td>APU0000FD3101</td>
      <td>1998-03-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1998-04-01</td>
      <td>3.098</td>
      <td>APU0000FD3101</td>
      <td>1998-04-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1998-05-01</td>
      <td>3.099</td>
      <td>APU0000FD3101</td>
      <td>1998-05-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>263</th>
      <td>2019-12-01</td>
      <td>3.391</td>
      <td>APU0000FD3101</td>
      <td>2019-12-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>264</th>
      <td>2020-01-01</td>
      <td>3.368</td>
      <td>APU0000FD3101</td>
      <td>2020-01-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>265</th>
      <td>2020-02-01</td>
      <td>3.419</td>
      <td>APU0000FD3101</td>
      <td>2020-02-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>266</th>
      <td>2020-03-01</td>
      <td>3.415</td>
      <td>APU0000FD3101</td>
      <td>2020-03-01</td>
      <td>Pork</td>
    </tr>
    <tr>
      <th>267</th>
      <td>2020-04-01</td>
      <td>3.673</td>
      <td>APU0000FD3101</td>
      <td>2020-04-01</td>
      <td>Pork</td>
    </tr>
  </tbody>
</table>
<p>268 rows × 5 columns</p>
</div>






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
    </tr>
    <tr>
      <th>Meat</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Beef</th>
      <td>1.287167</td>
    </tr>
    <tr>
      <th>Chicken</th>
      <td>0.767375</td>
    </tr>
  </tbody>
</table>
</div>


