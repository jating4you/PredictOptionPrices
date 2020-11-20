from stocker import Stocker

microsoft = Stocker('MSFT')
# Stock is an attribute of the microsoft object
stock_history = microsoft.stock
stock_history.head()

# A method (function) requires parentheses
microsoft.plot_stock()

microsoft.plot_stock(start_date = '2000-01-03',  end_date = '2018-01-16',  stats = ['Daily Change', 'Adj. Volume'],  plot_type='pct')

microsoft.buy_and_hold(start_date='1986-03-13',
                       end_date='2018-01-16', nshares=100)

microsoft.buy_and_hold(start_date='1999-01-05', 
                      end_date='2002-01-03', nshares=100)
model, model_data = microsoft.create_prophet_model()



# model and model_data are from previous method call
model.plot_components(model_data)
plt.show()

print(microsoft.weekly_seasonality)
microsoft.weekly_seasonality = True
print(microsoft.weekly_seasonality)


microsoft.changepoint_date_analysis()
