# Puppet to increase user limit of /etc/security/limits.conf

# Increase hard limit
exec { 'increase-hard-limit':
    command => 'sed -i "/holberton hard/s/5/65535/" /etc/security/limits.conf',
    path    => '/bin/',
}

# Increase soft limit
exec { 'increase-soft-limit':
    command => 'sed -i "/holberton soft/s/4/65535/" /etc/security/limits.conf',
    path    => '/bin/',
}
