# Drug Analyzer

## Introduction

You are a member of a biotechnology programming team that is responsible for creating a system for lab technicians, which will assist them with drug analysis. 

Your goal is to create the application that will let them input their findings into the system, provide a meaningful analysis and verify the correctness of the data that they have sent.

## Prerequisites

To complete this task, use `Python 3`.

## Task Details

Note: Please do *NOT* modify any tests unless specifically told to do so.

### Part 1

Your goal in this part is to implement the `app.drug_analyzer.DrugAnalyzer` class. It will be responsible for analyzing data like the data presented below:
```
+-----------+-------------+------------------+-------------+
|   pill_id | pill_weight | active_substance | impurities  |
+-----------+-------------|------------------|-------------|
|    L01-10 | 1007.67     | 102.88           | 1.00100     |
|    L01-06 |  996.42     | 99.68            | 2.00087     |
|    G02-03 | 1111.95     | 125.04           | 3.00004     |
|    G03-06 |  989.01     | 119.00           | 4.00062     |
+-----------+-------------+-------------+-------------+-----
```
* The initialization of the class can be done from Python's list of lists (or nothing) and stored in the instance 
variable called `data` as per example below:
```
>>> my_drug_data = [
...                 ['L01-10', 1007.67, 102.88, 1.00100],
...                 ['L01-06', 996.42, 99.68, 2.00087],
...                 ['G02-03', 1111.95, 125.04, 3.00100],
...                 ['G03-06', 989.01, 119.00, 4.00004]
... ]
>>> my_analyzer = DrugAnalyzer(my_drug_data)
>>> my_analyzer.data
[['L01-10', 1007.67, 102.88, 1.001], ['L01-06', 996.42, 99.68, 2.00087], ['G02-03', 1111.95, 125.04, 3.001], ['G03-06', 989.01, 119.0, 4.00004]]
>>> DrugAnalyzer().data
[]
``` 
* The class should also have an option to add single lists into the object. Adding a list to the `DrugAnalyzer` object 
should return a new instance of this object with an additional element. Adding improper type or a list with improper 
length should raise a `ValueError`. An example of a correct and wrong addition output is shown below:
```
>>> my_new_analyzer = my_analyzer + ['G03-01', 789.01, 129.00, 0.00008]
>>> my_new_analyzer.data
[['L01-10', 1007.67, 102.88, 1.001], ['L01-06', 996.42, 99.68, 2.00087], ['G02-03', 1111.95, 125.04, 3.001], ['G03-06', 989.01, 119.0, 4.00004], ['G03-01', 789.01, 129.0, 8e-05]]
>>> my_new_analyzer = my_analyzer + ['G03-01', 129.00, 0.00008]
Traceback (the most recent call is displayed as the last one):
  File "<stdin>", line 1, in <module>
ValueError: Improper length of the added list.
``` 

### Part 2
Implement the `verify_series` method inside the `app.drug_analyzer.DrugAnalyzer` class.

The goal of this method is to receive a list of parameters and use them to verify if the pills described inside the instance
variable `data` matches the given criteria. It should return a `Boolean` value as a result.

The function would be called as follows:
```
verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.001)
```
Where:
 * the `series_id` is a 3 characters long string that is present at the beginning of every `pill_id`, before the `-` sign, for example, `L01` is the `series_id` in `pill_id = L01-12`.
 * the `act_subst_wgt` is the expected weight (_mg_) of the active substance content in the given series in one pill.
 * the `act_subst_rate` is the allowed rate of difference in the active substance weight from the expected one
(`act_subst_wgt`). For example, for `100 mg`, the accepted values would be between `95` and `105`. This value must be in `(0; 1]` range.
 * the `allowed_imp` is the allowed rate of impure substances in the `pill_weight`. For example, for `1000 mg` pill_weight 
 and `0.001` rate, the allowed amount of impurities is `1 mg`. This value must be in `(0; 1]` range.
 
The function should take all pills that are part of the `L01` series, sum their weight and calculate if the 
amount of `active_substance`, as well as `impurities`, match the given rates. It should return `True` if both conditions
are met and `False` if any of them is not met.

The `False` result should mean that all the passed parameters are proper, but either the `active_substance` amount or the `impurities` amount
is improper.
In case of a `series_id` that is not present in the `data` at all or in case of any improper parameter, the function should throw a `ValueError`.

Example:
```
>>> my_drug_data = [
...                 ['L01-10', 1000.02, 102.88, 1.00100],
...                 ['L01-06', 999.90, 96.00, 2.00087],
...                 ['G02-03', 1000, 96.50, 3.00100],
...                 ['G03-06', 989.01, 119.00, 4.00004]
... ]
>>> my_analyzer = DrugAnalyzer(my_drug_data)
>>> my_analyzer.verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.001)
False
>>> // The overall active_substances weight would be 198.88, which is within the given rate of 0.05 for 200 mg (2 * act_subst_wgt).
>>> // However, the sum of impurities would be 3.00187, which is more than 0.001*1999.92 (allowed_imp_rate * (1000.02 + 999.90).
>>> my_analyzer.verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.01)
True
>>> my_analyzer.verify_series(series_id = 'B03', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.001)
Traceback (the most recent call is displayed as the last one):
  File "<stdin>", line 1, in <module>
ValueError: B03 series is not present within the dataset.
```

## Hints

You shouldn't modify the unit tests.

To execute the unit tests, use:

```
pip install -q -e . && python3 setup.py pytest
```
