# TicTacToy_SI

Function get_map_array is needed in neuron network. <br/>
It returns array of values -1, 0, 1.<br/>
	-1 - on this field is your opponent<br/>
	0 - is empty<br/>
	1 - on this field is your sign<br/>
	<br/>
It goes row by row for example:<br/>
<br/>
X | O | _<br/>
_ | X | _<br/>
_ | _ | _<br/>
<br/>
get_map_array('X') will print:<br/>
[1 -1 0 0 1 0 0 0 0]<br/>
