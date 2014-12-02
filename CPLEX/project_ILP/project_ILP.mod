/*********************************************
 * OPL 12.6.0.0 Model
 * Author: AbYosh
 * Creation Date: 4 Nov 2014 at 15:10:13
 *********************************************/

 int num_data_structures	= ...;	//	number of data structures
 int num_memory_banks 		= ...;	//	number of memory banks (m+1 = external memory)
 int p						= ...;	//	penalty
 int ext					= num_memory_banks+1;
 int conflicts				= ...;
 
 range n 		= 1..num_data_structures;
 range m 		= 1..num_memory_banks;
 range m_ext 	= 1..num_memory_banks+1;
 range o		= 1..conflicts;
 
 float d [k in o]	= ...;	//	conflict costs 
 float s [i in n] 	= ...;	//	size of data structure i
 float c [j in m] 	= ...;	//	capacity of memory bank j
 float e [i in n] 	= ...;	//	access cost of data structure i
 
 int A [k in o]		= ...;	//	first data structure in each conflict
 int B [k in o] 	= ...;	//	second data structure in each conflict
 
 dvar boolean x [i in n][j in m_ext];	//	binary matrix indication data structure in memory bank j
 dvar int y [k in o];					//	Status of the conflicts
 
 minimize 
 	sum(k in o)(y[k]*d[k]) + sum(i in n)sum(j in m)e[i]*x[i][j] + p*sum(i in n)e[i]*x[i][ext];
 		
 subject to {
 	
 	forall(i in n)					//	(3)
 	  sum(j in m_ext) x[i][j] == 1;
 	  
 	forall(j in m)					//	(4)
 	  sum(i in n) x[i][j]*s[i] <= c[j];
 	   
 	forall(j in m)					//	(5)
 	  forall (k in o)
 	      x[A[k]][j] + x[B[k]][j] <= 1+y[k];
 		    
 	forall(j in m)					//	(6)
 	  forall(k in o)
 	      x[A[k]][j] + x[B[k]][ext] <= 1+(1/p)*y[k];
 	      
 	forall(j in m)					//	(6)
 	  forall(k in o)
 	      x[A[k]][ext] + x[B[k]][j] <= 1+(1/p)*y[k];

 	forall(k in o)				//	(8)
 	  x[A[k]][ext] + x[B[k]][ext] <= 1+(1/(2*p))*y[k];
 
 	forall(k in o)
 	  y[k] >= 0;
 }
 
 //	POST-PROCESSING BLOCK
execute {
 
 for (var j=1; j<=num_memory_banks; j++) {
	var load=0;
 	for (var i=1; i<=num_data_structures; i++) {
	  	load = load + (s[i]*x[i][j]);
 }  	
  	load = load * (1/c[j]) * 100;
  	writeln("Load in Memory Bank " + j + " at " + load + " %");
   
 }   
 writeln("x = DataStructures \\ MemoryBanks");
 for (var i=1; i<=num_data_structures; i++) {
 write("[");
 	for (var j=1; j<=num_memory_banks+1; j++) { 
	  write(" "+x[i][j]+" ");
	}
	write("] Size of DataStructure = "+s[i]+"\n");
	
}  

writeln("\nConflicts Costs");
write("[\t");
for (var k=1; k<=conflicts; k++)
	write(y[k]+"\t");
write("]\n");



}; 