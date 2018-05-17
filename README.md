# Enron-Network

This project uses the emails from Enron Corperation. The emails are parsed by "parser.py" to only show "To" and "From" fields. The output file from  "parser.py" is then used by the Map-Reduce program "emailcount" using a Hadoop File System. The Output of "emailcount" shows not only how often a single person emails/is emailed, but also how often two people communicate using  key-value pairs. The key-value pairs are then used as input for the graphing program.
