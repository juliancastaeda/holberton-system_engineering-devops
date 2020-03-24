# Using Puppet, create a manifest that kills a process named killmenow.
# pkill is a linux command, therefore the path from the origin is indicated
exec { 'killmenow':
    command => '/usr/bin/pkill killmenow';
}