set_units -time ns -resistance kOhm -capacitance pF -voltage V -current uA

create_clock [get_ports clk] -name CLK -period 2.5
set_clock_uncertainty 0.15 [get_clocks CLK]
set_input_delay 1 -clock CLK [get_ports x]
set_output_delay 0.5 -clock CLK [get_ports y]
set_max_fanout 20 [current_design]
set_load 0.05 [all_outputs]
set_max_transition 0.1 [current_design]

################
create_clock [get_ports clk] -name MY_CLK -period 2
set_clock_uncertainty -setup 0.1 [get_clocks MY_CLK]
set_clock_uncertainty -hold 0.06 [get_clocks MY_CLK]

set_input_delay 0.6 [all_inputs]

set_output_delay 0.8 [all_outputs]

set_max_fanout 35 [current_design]
set_max_transition 0.05 [current_design]
set_load 0.04 [all_outputs]
