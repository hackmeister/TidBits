"""
TB aka TidBits is a small commandline utility for storing miscellaneous pieces of information.
It was built using SQLite as its database engine.
    tb -a - add new tidbit
    tb -l - list tidbits
    tb -d - delete tidbit
    tb -e - edit tidbit (Prompts for record number to edit.)
    tb -f - find tidbit (Accepts two arguments to search ex: tb -f vim copy)
Hope you find it useful.
"""

#Author: Jim Richards
#Program Name: TidBits
#Version: .1

import sqlite3, sys, os, datetime, getopt
from colorama import init, Fore

#os.system('clear')

tidbits = "Users/drdoall/tidbits.db"
conn = sqlite3.connect('/Users/drdoall1/tidbits.db')
c = conn.cursor()
now = datetime.datetime.now()
today =  now.strftime("%m-%d-%Y")


def main():
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'aldef',['add', 'list', 'delete', 'edit', 'find'])
    except getopt.GetoptError, err:
        #print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for opt, arg in options:
        if opt in ('-a', '--add'):
            addtb()
        elif opt in ('-l', '--list'):
            listtb()
        elif opt in ('-d', '--delete'):
            deltb()
        elif opt in ('-e', '--edit'):
            edittb()
        elif opt in ('-f', '--find'):
            findtb()

def usage():
    print ""
    print ""
    print ("Usage: ")
    print ""
    print "TidBit is a simple Command line app that uses SQLite as a database for storing"
    print "anything which can be stored using a title, tags and notes. I use it for documenting"
    print "web sites which I want to look at later"
    print ""
    print ""
    print "       -a     Add new TidBit."
    print "       -e     Edit TidBit."
    print "       -d     Delete TidBit."
    print "       -l     List all TidBits."
    print ""
    print ""
    print today
    sys.exit(1)

def addtb():
    init()
    os.system("clear")
    print ""
    title = raw_input("%sEnter Title:     " % Fore.YELLOW)
    print ""
    tbcat = raw_input("Enter Category:     ")
    print ""
    tags = raw_input("Enter Tags:     ")
    print ""
    note = raw_input("Enter TidBit:     ")
    #cursor.execute("INSERT INTO table VALUES (?, ?, ?)", (var1, var2, var3))
    c.execute("insert into tidbit values (?, ?, ?, ?, ?)", (today, title, tags, note, tbcat))
    conn.commit()
    c.close()
    return

def listtb():
    os.system("clear")
    c.execute("select rowid, * from tidbit")
    count = c.rowcount
    print "Record Count:     ", count
    for row in c:
            print '  ',Fore.WHITE + str(row[0]), '     ', row[1], '     ',Fore.RED + row[2]
            print ""
            init()
            print '                           ' + Fore.YELLOW + row[4]
#            print '                          %sNotes:' % Fore.YELLOW '%s' row[4] % Fore.RED
            print "%s_" % Fore.BLACK *30
    return

def deltb():
    os.system("clear")
    return

def edittb():
    os.system("clear")
    print ""
    rowid = raw_input(Fore.WHITE + "ID #:     " + Fore.RED)
    c.execute('select rowid, * from tidbit where rowid = ?', rowid)
    for row in c:
            print '-'*10
            print Fore.WHITE + 'ID:       ', Fore.RED + str( row[0] )
            print Fore.WHITE + 'Date:     ', Fore.RED + row[1]
            print Fore.WHITE + 'Title:    ', Fore.RED + row[2]
            print Fore.WHITE + 'Tags:     ', Fore.RED + row[3]
            print Fore.WHITE + 'Notes:    ', Fore.RED + row[4]
            print '-'*10
            title = raw_input(Fore.WHITE + "Enter Title:     " +  Fore.YELLOW)
            print ""
            tbcat = raw_input(Fore.WHITE + "Enter Category:     " + Fore.YELLOW)
            print ""
            tags = raw_input(Fore.WHITE + "Enter Tags:     " + Fore.YELLOW)
            print ""
            note = raw_input(Fore.WHITE + "Enter TidBit:     " + Fore.YELLOW)
            c.execute("update tidbit set title=?, tbcat=?, tags=?, note=? where rowid=?",(title, tbcat, tags, note, rowid))
            conn.commit()
            return

def findtb():
    os.system("clear")
    print ""
    tbcat = sys.argv[2]
    print tbcat
    c.execute('select rowid, * from tidbit where tbcat = ? collate nocase', [tbcat])
    for row in c:
        print 'Notes: ', row[4]
    return

#Create table
#c.execute('create table tidbit (date text, title text, note text)')

# Insert a row of data
#    c.execute("insert into tidbit values ('01-30-2012','HTML Kickstart', \
#            'HTML Kickstart is a complete library of resources for creating \
#            HTML user interfaces. See it here at http://www.99lime.com/')")



# Save (commit) the changes
#conn.commit()

# We can also close the cursor if we are done with it
#c.close()

if __name__ == "__main__":
        main()

