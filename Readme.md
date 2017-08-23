# ResophNotes.py

## About

While Resoph Notes runs fine via wine, I also want to access my notes on the
cmdline whether my bash runs on Linux, OS X or Windows (e.g. gitbash).

To accomplish that, I wrote a small Resoph Notes viewer in Python.

## License

This script has been released under the BSD License.

## Credits

Uses xmltodict.py written and copyrighted by Martin Blech:

https://github.com/martinblech/xmltodict/

```
Copyright (C) 2012 Martin Blech and individual contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
```

## Usage

```
$ ./ResophNotes.py --help
usage: ResophNotes.py [-h] [--data DATA] [--json JSON] [--cli] [--internal]

Convert to JSON and query ResophNotes notes from shell.

optional arguments:
  -h, --help   show this help message and exit
  --data DATA  Import from this ResophNotes data file. Default:
               resophnotesdata.xml
  --json JSON  JSON file with converted ResophNotes data. Default:
               resophnotesdata.json
  --cli        Open an interactive cli to query ResophNotes data.
  --internal   Use internal viewer instead of less.
```

## CLI Examples

### Convert resophnotesdata.xml

Resoph Notes stores all the notes in a xml file called resophnotesdata.xml.
This script parses the data file and converts it to JSON:

```
$ ./ResophNotes.py --data resophnotesdata.xml --json resophnotesdata.json
```

### Query Resoph Notes texts via commandline

```
$ ./ResophNotes.py --cli

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|R|e|s|o|p|h|N|o|t|e|s|.|p|y|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Total number of notes: 1
Most common tags: @foo:1, @bar:1, @example:1

Query (q to quit)? example
0 | 2017-19-18 05:31:10 | resophnotes.py - example note | tags: @foo @bar 
@example
Results: 1
Read which note (q to return)? 1
Read which note (q to return)? q
Query (q to quit)? q
```

### A more realistic example

```
$ ./ResophNotes.py --cli

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|R|e|s|o|p|h|N|o|t|e|s|.|p|y|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Total number of notes: 217
Most common tags: @tipps:63, @****x:36, @security:35, @****m:34, @docs:27, 
@rfc:27, @r***l:22, @****tos:21, @d***cer:21, @oneliner:20

Query (q to quit)? rfc
0 | 2017-06-17 19:49:49 | RFC 1123 (STD 3) — Requirements for Internet Hosts - Application and support | tags: @rfc
1 | 2017-06-17 19:51:15 | RFC 1112 (STD 5) — Host extensions for IP multicasting | tags: @rfc
2 | 2017-06-17 19:58:48 | RFC 826 (STD 37) — Ethernet Address Resolution Protocol | tags: @rfc
3 | 2017-06-17 19:55:33 | RFC 1034 (STD 13) — Domain names - concepts and facilities | tags: @rfc
4 | 2017-06-17 19:54:23 | RFC 1870 (STD 10) — SMTP Service Extension for Message Size Declaration | tags: @rfc
5 | 2017-06-17 19:51:34 | RFC 768 (STD 6) — User Datagram Protocol | tags: @rfc
6 | 2017-06-17 19:52:10 | RFC 793 (STD 7) — Transmission Control Protocol | tags: @rfc
7 | 2017-19-11 11:49:59 | *************
8 | 2017-06-17 19:53:46 | RFC 821 (STD 10) — Simple Mail Transfer Protocol | tags: @rfc
9 | 2017-06-14 08:12:19 | ************
10 | 2017-06-17 19:56:58 | RFC 1157 (STD 15) — A Simple Network Management Protocol | tags: @rfc
11 | 2017-06-17 19:50:38 | RFC 792 (STD 5) — Internet Control Message Protocol | tags: @rfc
12 | 2017-06-17 19:56:16 | RFC 1035 (STD 13) — Domain names - implementation and specification | tags: @rfc
13 | 2017-06-17 19:49:21 | RFC 1122 (STD 3) — Requirements for Internet Hosts - Communication layers | tags: @rfc
14 | 2017-06-17 19:56:36 | RFC 974 (STD 14) — Mail routing and the domain system | tags: @rfc
15 | 2017-06-17 19:48:51 | RFC 1700 (STD 2) — Assigned Numbers | tags: @rfc
16 | 2017-06-17 19:54:54 | RFC 822 (STD 11) — Standard for the format of ARPA Internet text messages | tags: @rfc
17 | 2017-06-17 19:48:15 | RFC 5000 (STD 1) — Internet Official Protocol Standard | tags: @rfc
18 | 2017-06-17 19:55:17 | RFC 1049 (STD 11) — Content-type header field for Internet messages | tags: @rfc
19 | 2017-06-17 19:57:42 | RFC 1155 (STD 17) — Structure and Identification of Management Information for TCP/IP-based Internets | tags: @rfc
20 | 2017-06-17 19:53:02 | RFC 855 (STD 8) — Telnet option specifications | tags: @rfc
21 | 2017-06-17 19:53:22 | RFC 959 (STD 9) — File Transfer Protocol | tags: @rfc 22 | 2017-06-17 08:01:22 | RFC 4251 — The Secure Shell (SSH) Protocol Architecture | tags: @rfc
23 | 2017-06-17 19:52:33 | RFC 854 (STD 8) — Telnet Protocol specification | tags: @rfc
24 | 2017-06-17 19:50:18 | RFC 791 (STD 5) — Internet Protocol | tags: @rfc
25 | 2017-06-17 19:58:27 | RFC 1350 (STD 33) — The TFTP Protocol (Revision 2) | tags: @rfc
26 | 2017-06-14 19:57:36 | ***************
27 | 2017-06-17 19:57:16 | RFC 1212 (STD 16) — Concise MIB Definitions | tags: @rfc
28 | 2017-06-17 19:54:05 | RFC 1869 (STD 10) — SMTP Service Extensions | tags: @rfc
29 | 2017-06-17 19:59:13 | RFC 903 (STD 38) — Reverse Address Resolution Protocol | tags: @rfc
Results: 30
Read which note (q to return)?
```
