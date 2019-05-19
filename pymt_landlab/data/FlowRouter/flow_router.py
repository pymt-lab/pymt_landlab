FlowRouter:
  method: {{ method }}
  runoff_rate: {{ runoff_rate }}

clock:
  start: {{ clock_start }}
  stop: {{ clock_stop }}
  step: {{ clock_step }}
  units: ""
grid:
  RasterModelGrid:
    args: [{{ grid_rows }}, {{ grid_columns }}]
    xy_spacing: [{{ grid_column_spacing }}, {{ grid_row_spacing }}]
    fields:
      node:
        topographic__elevation:
          - constant:
              value: 0.0
