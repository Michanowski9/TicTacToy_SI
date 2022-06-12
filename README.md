# TicTacToy_SI

Function get_map_array is needed in neuron network. <br/>
It returns array of values -1, 0, 1.<br/>
&emsp;&emsp;-1 - on this field is your opponent<br/>
&emsp;&emsp;0 - is empty<br/>
&emsp;&emsp;1 - on this field is your token<br/>
<br/>
It goes row by row for example:<br/>
<br/>
&emsp;&emsp; x | o | _<br/>
&emsp;&emsp; _ | _ | _<br/>
&emsp;&emsp; _ | x | _<br/>
<br/>
get_map_array('X') will return:<br/>
[1 -1 0 0 1 0 0 0 0]<br/>
