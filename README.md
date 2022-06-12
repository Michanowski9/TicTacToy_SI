# TicTacToy_SI

Function get_map_array is needed in neuron network. 
It returns array of values -1, 0, 1.
	-1 - on this field is your opponent
	0 - is empty
	1 - on this field is your sign
	
It goes row by row for example:

X | O | _
_ | X | _
_ | _ | _

get_map_array('X') will print:
[1 -1 0 0 1 0 0 0 0]
