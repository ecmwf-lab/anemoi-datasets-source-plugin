# Anemoi plugin example


## Installation

pip install <this-package>

Then additional features (filters,...) become available on anemoi.


## Custom filter

Runs a custom filter with options

```yaml
    dates:
      start: 2020-12-30 00:00:00
      end: 2021-01-03 12:00:00
      frequency: 12h

    input:
      pipe:
        - join:
          - mars:
              expver: "0001"
              class: ea
              grid: 20./20.
              param: [2t]
              levtype: sfc

          -  mars:
              expver: "0001"
              class: ea
              grid: 20./20.
              param: [q]
              levtype: pl
              level: [50]
              stream: oper
              type: an
    
        - custom-filter:
            a: 2t

```


Output:

```
   Index │ Variable    │         Min │         Max │        Mean │       Stdev
   ──────┼─────────────┼─────────────┼─────────────┼─────────────┼────────────
       0 │ 2t          │       226.4 │     307.421 │     277.946 │     19.1507
       1 │ 2t_modified │       452.8 │     614.843 │     555.892 │     38.3014
       3 │ q_50        │ 1.30264e-06 │ 3.22996e-06 │ 2.86295e-06 │ 2.06885e-07
   ──────┴─────────────┴─────────────┴─────────────┴─────────────┴────────────

```



## tests

cd tests && ./test.sh
