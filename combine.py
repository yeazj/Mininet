#!/usr/bin/env python


user_f = "/usr/share/metasploit-framework/data/wordlists/unix_users.txt"
pass_f = "/usr/share/metasploit-framework/data/wordlists/unix_passwords.txt"

pass_list = []

with open(pass_f, "r") as passf:
	for p in passf:
		pass_list.append(p)

with open(user_f, "r") as userf:
	with open("userpass.txt", "w") as f:
		userf.readline()
		for user in userf:
			for p in pass_list:
				tmp = user.strip() + " " + p
				f.write(tmp)

