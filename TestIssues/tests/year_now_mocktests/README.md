## Тестирование what-is-year-now

В терминале, находясь в директории ```test_issues``` выполнить команду:
```
cd tests/year_now_mocktests; pytest --cov what_is_year_now -v test_what_is_year_now.py --cov-report=html:html_report > result.txt; cd ../../
```
Эта команда проведёт тестирование и его результаты запишет в файл ```result.txt``` в директории ```test_issues/tests/year_now_mocktests/```
