import json
import requests
from django.shortcuts import render



def candlestick_chart(request):
    api_key = 'Y9KX89CF348WX1SU'
    symbol = 'IBM'
    interval = '5min'
    
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}'
    
    response = requests.get(url)
    data = response.json()
    time_series = data['Time Series (5min)']
    
    chart_data = []
    for timestamp, values in time_series.items():
        chart_data.append({
            'time': timestamp,
            'open': float(values['1. open']),
            'high': float(values['2. high']),
            'low': float(values['3. low']),
            'close': float(values['4. close'])
        })
    
    chart_data.sort(key=lambda x: x['time'])
    
    context = {
        'chart_data': json.dumps(chart_data),
        'symbol': symbol
    }
    
    return render(request, 'candlestick_chart.html', context)

