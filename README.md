# Anemoi plugin example


## Installation

pip install <this-package>

Then additional features (filters,...) become available on anemoi.


## Custom filter 2 (recommended)

Runs a custom filter with options, this filter process the data by smaller groups of
fields with matching metadata.

See `./anemoi_plugin_example/filter2.py` and `./custom2.yaml`

```yaml
    dates:
      start: 2020-12-30 00:00:00
      end: 2021-01-03 12:00:00
      frequency: 12h

    input:
      pipe:
        - some-source:
            arg1: x
            arg2: x
        - custom-filter-2:
            a: q
```

Output:

```
   Index │ Variable      │         Min │         Max │        Mean │       Stdev
   ──────┼───────────────┼─────────────┼─────────────┼─────────────┼────────────
       0 │ 2t            │       226.4 │     307.421 │     277.946 │     19.1507
       1 │ 2t_modified_2 │        2264 │     3074.21 │     2779.46 │     191.507
       2 │ msl           │     94364.8 │      106024 │      100890 │     1658.14
       3 │ q_100         │ 1.03281e-06 │ 4.68307e-06 │ 2.65373e-06 │ 5.43983e-07
       4 │ q_50          │ 1.30264e-06 │ 3.22996e-06 │ 2.86295e-06 │ 2.06885e-07
   ──────┴───────────────┴─────────────┴─────────────┴─────────────┴────────────
```

## Custom filter (advanced usage)

Runs a custom filter with options, this filter process batches of data, all together.
The result is the same as the previous filter.

See `./anemoi_plugin_example/filter.py` and `./custom.yaml`

```yaml
    dates:
      start: 2020-12-30 00:00:00
      end: 2021-01-03 12:00:00
      frequency: 12h

    input:
      pipe:
        - some-source:
            arg1: x
            arg2: x

        - custom-filter:
            a: 2t
```


Output:

```
   Index │ Variable    │         Min │         Max │        Mean │       Stdev
   ──────┼─────────────┼─────────────┼─────────────┼─────────────┼────────────
       0 │ 2t          │       226.4 │     307.421 │     277.946 │     19.1507
       1 │ 2t_modified │       452.8 │     614.843 │     555.892 │     38.3014
       2 │ msl         │     94364.8 │      106024 │      100890 │     1658.14
       3 │ q_100       │ 1.03281e-06 │ 4.68307e-06 │ 2.65373e-06 │ 5.43983e-07
       4 │ q_50        │ 1.30264e-06 │ 3.22996e-06 │ 2.86295e-06 │ 2.06885e-07
   ──────┴─────────────┴─────────────┴─────────────┴─────────────┴────────────
```

## tests

cd tests && ./test.sh
