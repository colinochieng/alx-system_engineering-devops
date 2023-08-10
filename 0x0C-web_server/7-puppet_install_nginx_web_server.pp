# configuring your server with Puppet

exec { 'updates needed':
  command => 'apt update',
  path    => '/usr/bin:/usr/sbin:/bin'
}

package { 'nginx':
  ensure          => installed,
  install_options => ['-y'],
  provider        => 'apt',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html':
  ensure => directory,
  mode   => '0755',
}

file { '/var/www':
  ensure  => directory,
  mode    => '0755',
  recurse => true,
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello world!\n',
  mode    => '0644',
  require => File['/var/www/html'],
}

file { '/var/www/html/custom_404.html':
  content => "Ceci n'est pas une page",
  mode    => '0644',
  require => File['/var/www/html'],
}

file { '/etc/nginx/sites-available/default':
  content => @(END),
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files $uri $uri/ =404;
                rewrite ^/redirect_me(.*)$ https://www.youtube.com/watch?v=70JD5YTemJc permanent;
        }

        error_page 404 /custom_404.html;
        location = /custom_404.html {
                internal;
        }
}
END
  require => Package['nginx'],
  notify  => Service['nginx'],
}

