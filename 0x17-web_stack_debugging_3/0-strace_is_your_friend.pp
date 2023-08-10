#fixing 500 web error

package { 'sed':
  ensure => installed,
}

exec { 'Fixes':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Package['sed'],
}
