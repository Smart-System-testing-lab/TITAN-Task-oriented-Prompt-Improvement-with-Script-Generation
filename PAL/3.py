def solution():
    deferred_tax_assets_2014 = 6348
    deferred_tax_assets_2013 = 6241
    regulatory_assets_2014 = 6348
    regulatory_assets_2013 = 6241

    deferred_tax_assets_change = (deferred_tax_assets_2014 - deferred_tax_assets_2013) / deferred_tax_assets_2013
    regulatory_assets_change = (regulatory_assets_2014 - regulatory_assets_2013) / regulatory_assets_2013

    print(f"Deferred tax assets: {deferred_tax_assets_change:.4f}%")
    print(f"Regulatory assets: {regulatory_assets_change:.4f}%")

    return deferred_tax_assets_change, regulatory_assets_change


"""
                Sure, here's a Python function that calculates the percentage change in deferred tax assets and regulatory assets from 2013 to 2014 using the information provided:
```python
def solution():
    deferred_tax_assets_2014 = 6348
    deferred_tax_assets_2013 = 6241
    regulatory_assets_2014 = 6348
    regulatory_assets_2013 = 6241

    deferred_tax_assets_change = (deferred_tax_assets_2014 - deferred_tax_assets_2013) / deferred_tax_assets_2013
    regulatory_assets_change = (regulatory_assets_2014 - regulatory_assets_2013) / regulatory_assets_2013

    print(f"Deferred tax assets: {deferred_tax_assets_change:.4f}%")
    print(f"Regulatory assets: {regulatory_assets_change:.4f}%")

    return deferred_tax_assets_change, regulatory_assets_change
```
This function takes no input, as all the necessary values are provided in the question. It calculates the percentage change in deferred tax assets and regulatory assets using the formula you provided, and then prints the results.

Here's an explanation of the code:

* `deferred_tax_assets_2014` and `deferred_tax_assets_2013` are the values of deferred tax assets for 2014 and 2013, respectively.
* `regulatory_assets_2014` and `regulatory_assets_2013` are the values of regulatory assets for 2014 and 2013, respectively.
* `deferred_tax_assets_change` is the percentage change in deferred tax assets from 2013 to 2014. It's calculated by subtracting the value of deferred tax assets in 2013 from the value in 
"""

solution()