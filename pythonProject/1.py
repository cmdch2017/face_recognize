import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv('test.csv')
data = data[['Value']].values.astype(float)

# Data normalization
scaler = MinMaxScaler()
data = scaler.fit_transform(data)

# Prepare training data
seq_length = 12  # Set the time window length
X = []
y = []
for i in range(len(data) - seq_length):
    X.append(data[i:i+seq_length])
    y.append(data[i+seq_length])

X = np.array(X)
y = np.array(y)

# Split into training and test sets
train_size = int(len(data) * 0.80)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Create and compile the RNN model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=2)

# Predict the housing price trend for the next two years
forecast = []
for i in range(len(X_test)):
    current_batch = X_test[i].reshape((1, seq_length, 1))
    current_pred = model.predict(current_batch)[0, 0]
    forecast.append(current_pred)

# Inverse transform the forecasted results
forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))

# Plot the forecasted results
plt.figure(figsize=(12, 6))
plt.plot(range(len(y_test)), y_test, label='Actual Data')
plt.plot(range(len(y_test)), forecast, label='Forecasted Data')
plt.legend()
plt.title('Housing Price Trend Forecast')
plt.xlabel('Time')
plt.ylabel('Price')
plt.show(block=False)
plt.pause(3)  # Display the plot for 3 seconds
plt.close()
