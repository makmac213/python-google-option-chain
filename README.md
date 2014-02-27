python-google-option-chain
==============

$ pip install python-google-option-chain


Sample Usage
============

from optionchain import OptionChain

oc = OptionChain('NASDAQ:AAPL')

oc.to_excel() # outputs puts and calls in an excel sheet

oc.puts

oc.calls


