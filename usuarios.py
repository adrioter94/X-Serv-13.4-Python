#!/usr/bin/python

fich = open("/etc/passwd", "r");
usuarios = fich.readlines();

for usuario in usuarios:
    print "usuario-> " +  usuario.split(':')[0] + ", shell-> " + usuario.split(':')[-1];

print "Numero de usuarios: " + str(len(usuarios));
fich.close();
