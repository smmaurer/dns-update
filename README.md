# dns-update

Cron script for dynamic DNS. 

This is a simple Python script that checks your IP address, and if it has changed updates a DNS A-record.

Uses the [DNS-Lexicon](https://dns-lexicon.readthedocs.io/) command line tool, which supports all the main DNS hosts.
