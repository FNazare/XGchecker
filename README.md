# XGchecker
A simple tool to verify if all the XG elements in an iTX Channel Schedule (an .itxml file) are valid, according to a pre-defined list (a .csv file).

### Usage:
```bash
XGchecker.py <inputfile.itxml> <valid_XG_list.csv>
```

### Output example:
```
Invalid Template name: [XG_QADRO] at 2021-06-10T07:13:26.9200000

Checked if every XG in Schedule is one of these:
{'XG_NEXT', 'XG_CH1_LOGO', 'XG_QUADRO'}

4 templates checked.
invalid: 1
valid: 3
```
