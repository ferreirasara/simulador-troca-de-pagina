# simulador-troca-de-pagina

## Running the simulator

In the src folder, run the core.py file, along with the name of the configuration file.

Example: `python core.py settings1.txt`

## Configuration File
The configuration file must have the following structure:

* 1st line: memory size.
* 2nd line: Initial memory status. (Use `0` to represent empty positions, if any).
* 3rd line: Queue of processes to be executed.
* 4th line: Action to be taken for each process (`R` for read or `W` for write).

Use `|` to represent each processor clock.

## About the simulator

To simulate memory, a class was used that has an attribute called memory, with the following structure:

```python
memory = {
	'lenght': memory lenght,
	'memory': [
		[
		    process,
		    valid,
		    present,
		    referenced,
		    modified,
		    frame/disk
		]
	]
}
```

To manage the free spaces, a greedy algorithm was used, which runs through the memory from beginning to end and takes the first free space it finds.

The following page exchange algorithms were implemented:

* Optimal Algorith
* FIFO
* Second Chance
* LRU
* NRU
