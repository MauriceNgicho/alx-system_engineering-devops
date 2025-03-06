# puppet code that increases nginx default to 496

# Increase ULIMIT
exec { 'increase-ulimit':
    command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
}

# Restart nginx to update changes
exec { 'restert-nginx':
    command => '/usr/sbin/service nginx restart',
}
