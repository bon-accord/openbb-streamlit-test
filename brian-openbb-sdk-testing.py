#!/usr/bin/env python3
from datetime import date, datetime, timedelta
import mplfinance as fplt
from openbb_terminal.sdk import openbb
import os

# What stock tickers are we interested in
tickers = [
    'RICA.L',
    'GCL.L',
    'PSRW.L'
]

# Set out some directories for the content we will render
render_parent_path = 'rendered'
render_image_path = f'{render_parent_path}/images'
if not os.path.exists(render_parent_path):
    os.makedirs(render_parent_path)
if not os.path.exists(render_image_path):
    os.makedirs(render_image_path)

# Establish our historic date stamp
now = date.today()
one_year_prior = datetime.now() - timedelta(365)
one_year_prior_str = one_year_prior.strftime('%Y-%m-%d')

# Use openbb to get our data and then fplt to plot the data as png files
for ticker in tickers:
    ticker_data = openbb.stocks.load(symbol=ticker, start_date = one_year_prior)
    fplt.plot(
        ticker_data,
        type='candle',
        style='charles',
        ylabel='Price (£)',
        volume=True,
        ylabel_lower='Vol',
        savefig=f"{render_image_path}/{ticker.replace('.', '_')}"
    )
