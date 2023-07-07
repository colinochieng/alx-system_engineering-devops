# Puppet code to make Nginx be run, and listen on port 80 of all the server's active IPv4 IPs
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }

  firewall { '100 allow nginx http':
    proto  => tcp,
    port   => 80,
    action => accept,
  }
}

include nginx
