# Conv

<h2>Background</h2>
<hr />
This program was created to fix a problem within an aplication created for Migration (DNM - Uruguay) and its counterpart in Argentina. 
The problem itself was a modyfication in the structure of an .xml file that Uruguay received from Argentina. 
This recurring problem was on-going for around 10 months (until this fix was created). 

<h2>Logic Behind it</h2> 
The aplication is in 3 parts.:
- Reading the .XML file
- Manipulate the results in memory
- Writes an .XML file with the structure needed for another program

<h3>Highlights!</h3>
- Reduced around 20% - 30% of the workload 
- Kept the information without touching it or modifying it
- Maintained information integrity

<h4>Future Refactor</h4>
** This is just a list about things to improve**
- Divide the file in 3 parts (Input, Logic, Output)
- Instead of using keys as part of the logic (specifically created for this app), it should be more practical and more generic to work with args[] and attributes created form the xml file itself.
- Probably a graph or a statistic based in a specifically chosen attribute from the xml file.
