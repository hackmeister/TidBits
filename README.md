##README.md
Program Title: TidBits<br />
Author: Jim Richards<br />
Release Date: 2/14/2012<br />
Version: .02<br />
<br />
TidBits is written in Python and has been designed to be a simple command line tool that allows you to store and retrieve little tidbits of information fast. It uses SQLite to store and retrieve information. The database consists of five fields.

	1.) Date
	2.) Title
	3.) Category
	4.) Tags
	5.) Note

Tidbits uses command line switches to accomplish most everything you need.

	-a Add Record
	-f Find Record
	-e Edit Record
	-d Delete Record
	-l List Records

Requirements:<br />
	SQLite 3<br />
	Colorama<br />  


On first execution it creates tidits.db in your $HOME directory. 

	Future:
	1.) Send list to browser
	2.) Create Flash Cards
