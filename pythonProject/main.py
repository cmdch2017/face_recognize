import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Combined dataset
data = [
    [pd.to_datetime('2023-09-01'), 46148],
    [pd.to_datetime('2023-08-01'), 46148],
    [pd.to_datetime('2023-07-01'), 47533],
    [pd.to_datetime('2023-06-01'), 47111],
    [pd.to_datetime('2023-05-01'), 46164],
    [pd.to_datetime('2023-04-01'), 46230],
    [pd.to_datetime('2023-03-01'), 49067],
    [pd.to_datetime('2023-02-01'), 49067],
    [pd.to_datetime('2023-01-01'), 49067],
    [pd.to_datetime('2022-12-01'), 50629],
    [pd.to_datetime('2022-11-01'), 49842],
    [pd.to_datetime('2022-10-01'), 55086],
    [pd.to_datetime('2022-09-01'), 52500],
    [pd.to_datetime('2022-08-01'), 47764],
    [pd.to_datetime('2022-07-01'), 42097],
    [pd.to_datetime('2022-06-01'), 41823],
    [pd.to_datetime('2022-05-01'), 40075],
    [pd.to_datetime('2022-04-01'), 40075],
    [pd.to_datetime('2022-03-01'), 40665],
    [pd.to_datetime('2022-02-01'), 41881],
    [pd.to_datetime('2022-01-01'), 36530],
    [pd.to_datetime('2021-12-01'), 38371],
    [pd.to_datetime('2021-11-01'), 49265],
    [pd.to_datetime('2021-10-01'), 50304],
    [pd.to_datetime('2021-09-01'), 46800],
    [pd.to_datetime('2021-08-01'), 41800],
    [pd.to_datetime('2021-07-01'), 42174],
    [pd.to_datetime('2021-06-01'), 51697],
    [pd.to_datetime('2021-05-01'), 51723],
    [pd.to_datetime('2021-04-01'), 45238],
    [pd.to_datetime('2021-03-01'), 45238],
    [pd.to_datetime('2021-02-01'), 46257],
    [pd.to_datetime('2021-01-01'), 46257],
    [pd.to_datetime('2020-12-01'), 44157],
    [pd.to_datetime('2020-11-01'), 43916],
    [pd.to_datetime('2020-10-01'), 45505],
    [pd.to_datetime('2020-09-01'), 45618],
    [pd.to_datetime('2020-08-01'), 46757],
    [pd.to_datetime('2020-07-01'), 46500],
    [pd.to_datetime('2020-06-01'), 46233],
    [pd.to_datetime('2020-05-01'), 45011],
    [pd.to_datetime('2020-04-01'), 44263],
    [pd.to_datetime('2020-03-01'), 44263],
    [pd.to_datetime('2020-02-01'), 44819],
    [pd.to_datetime('2020-01-01'), 44720],
    [pd.to_datetime('2019-12-01'), 44798],
    [pd.to_datetime('2019-11-01'), 44548],
    [pd.to_datetime('2019-10-01'), 44741],
    [pd.to_datetime('2019-09-01'), 44774],
    [pd.to_datetime('2019-08-01'), 43790],
    [pd.to_datetime('2019-07-01'), 43924],
    [pd.to_datetime('2019-06-01'), 43924],
    [pd.to_datetime('2019-05-01'), 42516],
    [pd.to_datetime('2019-04-01'), 42523],
    [pd.to_datetime('2019-03-01'), 41164],
    [pd.to_datetime('2019-02-01'), 41740],
    [pd.to_datetime('2019-01-01'), 42295],
    [pd.to_datetime('2018-12-01'), 40278],
    [pd.to_datetime('2018-11-01'), 38514],
    [pd.to_datetime('2018-10-01'), 37859],
    [pd.to_datetime('2018-09-01'), 37723],
    [pd.to_datetime('2018-08-01'), 37496],
    [pd.to_datetime('2018-07-01'), 38952],
    [pd.to_datetime('2018-06-01'), 39142],
    [pd.to_datetime('2018-05-01'), 40121],
    [pd.to_datetime('2018-04-01'), 41241],
    [pd.to_datetime('2018-03-01'), 41763],
    [pd.to_datetime('2018-02-01'), 40589],
    [pd.to_datetime('2018-01-01'), 40545],
    [pd.to_datetime('2017-12-01'), 40249],
    [pd.to_datetime('2017-11-01'), 41210],
    [pd.to_datetime('2017-10-01'), 41119],
    [pd.to_datetime('2017-09-01'), 40795],
    [pd.to_datetime('2017-08-01'), 41045],
    [pd.to_datetime('2017-07-01'), 41273],
    [pd.to_datetime('2017-06-01'), 40750],
    [pd.to_datetime('2017-05-01'), 36696],
    [pd.to_datetime('2017-04-01'), 36446],
    [pd.to_datetime('2017-03-01'), 36613],
    [pd.to_datetime('2017-02-01'), 34121],
    [pd.to_datetime('2017-01-01'), 33406],
    [pd.to_datetime('2016-12-01'), 33375],
    [pd.to_datetime('2016-11-01'), 33067],
    [pd.to_datetime('2016-10-01'), 32035],
    [pd.to_datetime('2016-09-01'), 31315],
    [pd.to_datetime('2016-08-01'), 30644],
    [pd.to_datetime('2016-07-01'), 28941],
    [pd.to_datetime('2016-06-01'), 28058],
    [pd.to_datetime('2016-05-01'), 27925],
    [pd.to_datetime('2016-04-01'), 26139],
    [pd.to_datetime('2016-03-01'), 24731],
    [pd.to_datetime('2016-02-01'), 22797],
    [pd.to_datetime('2016-01-01'), 22379],
]
# Create a DataFrame
df = pd.DataFrame(data, columns=['Date', 'Data'])

# Set the date column as the index
df.set_index('Date', inplace=True)

# Visualize the provided data
plt.figure(figsize=(12, 6))
plt.plot(df, label='Provided Data')
plt.title('Data Time Series')
plt.xlabel('Date')
plt.ylabel('Data')
plt.grid(True)

# Fit SARIMA model
order = (1, 1, 1)  # SARIMA model parameters, adjust as needed
seasonal_order = (1, 1, 1, 12)  # Seasonal parameters, adjust as needed

model = sm.tsa.SARIMAX(df, order=order, seasonal_order=seasonal_order)
results = model.fit()

# Generate future forecasts
forecast_steps = 3  # Forecast data for the next 3 months

# Get the predicted mean
forecast_mean = results.get_forecast(steps=forecast_steps).predicted_mean

# Create forecast date range starting from September 2023
forecast_dates = pd.date_range(start='2023-09-01', periods=forecast_steps, freq='MS')

# Combine the existing data and forecasted data
combined_data = pd.concat([df['Data'], pd.Series(forecast_mean, index=forecast_dates)])

# Visualize the combined data
plt.figure(figsize=(12, 6))
plt.plot(combined_data.index, combined_data.values, label='Combined Data')
plt.title('Data and Forecast')
plt.xlabel('Date')
plt.ylabel('Data')
plt.legend()
plt.grid(True)

# Save the entire chart as an image
plt.savefig('data_and_forecast.png')

print("Forecasted data for the next 3 months:")
print(forecast_mean)