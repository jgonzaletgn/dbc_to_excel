# dbc-to-excel

Tool to convert from a ``.dbc`` file to ``.xlsx`` Excel file using Python. The sofware is divided in three files:

* ``main.py`` is the main file.
* ``dbc_to_dataframe.py`` is the function to convert from ``.dbc`` file o a pandas dataframe.
* ``save_to_excel.py`` is the function to save the dataframe in Excel file ``.xlsx``.

# Dependencies

* [``cantools``](https://pypi.org/project/cantools/)
* [``pandas``](https://pypi.org/project/pandas/)
* [``openpyxl``](https://pypi.org/project/openpyxl/)



# Usage

Install the dependencies if you don't have them yet, using:

```bash
pip install cantools pandas openpyxl
```
Make sure the three files (``dbc_to_dataframe.py``, ``save_to_excel.py``, ``main.py``) are in the same directory.

Run ``main.py`` from the terminal or the development environment you are using:

```
python main.py
```

