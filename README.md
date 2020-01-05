# File Management Component
The purpose of this project is to build the file management component of distributed file management system. It's goal is to build the structure for file management to provide access to user(s) to create, delete, update and query files in the system. It gives a practical understanding of how different operating system concepts like paging, memory management, file search, file read and write etc work.

## Concepts Used
  Major programming concepts used are: file handling, string manipulation etc. <br/>
  More implementation details can be found in the [implementation.txt](/implementation.txt) file

## Working
  See the output and working of major features [here](/output)
## Features
Some of the features implemented in the file system are
  * Create(fname)
  * Delete(fname)
  * Mkdir(dirName)
  * chDir(dirName)
  * Move(source_fname, target_fname)
  * Write_to_file(fName, text), write_to_file(fname,write_at ,text)
  * Read_from_file(fname), Read_from_file(fname,start,size)
  * Truncate_file(fname,maxSize)
  * Show memory map
 
 ## Explanation of features

  * The action to create creates a file entry in your file structure. This may or may not include creating space in your disk.
  * Delete should remove the file form your file structure. This may or may not mean deleting the actual content of the file
  * Move should change the association of file in the directory structure and must not require physical movement of the content.
  * Write to a file should be through a function and should have two modes. 
    * Append mode writes to end of the file and write_at should write at a specific point in the file.  
    * The write_att may overwrite data at the location specified.  
  * Read from a file has two modes
    * sequential access reads from first word and returns the entire content
    * readFrom(start,size) reads from the start memory location for size number of characters.
  * Truncatefile(size) reduces the size of the file to size. Data within the file in memory location after size is deleted.
  * Show memory map shows the distribution of files in the memory.
  * The system must maintain persistent data. However, it creates a single data file which contains all the internal structure and data of the user created files.
  * The positive change of the size of the file is automatic, that is if more data is written on a file, or data is moved within a file to new location then the size is automatically increased.
  


