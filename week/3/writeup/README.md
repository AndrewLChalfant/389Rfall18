Writeup 3 - OSINT II, OpSec and RE
======

Name: Andrew Chalfant
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 3 Writeup

### Part 1 (100 pts)
Suggestions:

1. Fred Krueger's password to connect to the server was 'pokemon' which is not strong enough. This is problematic since it allows for easy access to sensitive company information, especially if the attacker did some background research on Fred's social media accounts. Fred could improve this password by adding special characters or symbols, so that a brute force attack would take longer and his password wouldn't be found in common password lists (he should probably change his username too). Fred could use a RSA token or some other form of 2FA to protect his account.

2. Fred should whitelist approved IPs to connect to the web server and admin server. Allowing random traffic and users to attempt to connect to the servers is a unnecessary risk that could lead to infiltration of Cornerstone Airlines servers. Fred could pretty easily block any traffic not from a internal or company network with a firewall. Buying a firewall or security service would be a lot cheaper than the cost of the company website being hacked.

3. Lastly, Fred should make sure he doesn't have any open and exposed ports on either of his servers. These provide attackers an easy way starting point for a potential attack and can easily be closed. I'd encourage Fred to run nmap or check his server settings before deploying anything into production. Additionally, having an page that's "under construction" is a great way to let attackers know your site might be vulnerable. Fred should remember to harden the server before deployment!   




