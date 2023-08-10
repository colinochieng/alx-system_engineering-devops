# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on

exec { 'update and upgrade the system':
  command  => 'apt update && apt install -y nginx',
  path     => '/bin/bash:/usr/bin/bash:/bin',
  provider => 'shell',
}

package { 'nginx':
  ensure          => installed,
  install_options => ['-y'],
  provider        => 'apt',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => "Hello world!\n",
}

file { '/var/www/html/custom_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  require => Package['nginx'],
  notify  => Service['nginx'],
  content => "
  server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # Add custom header
        add_header X-Served-By $hostname;

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
#       location ~ /redirect_me {
#               return 301 https://www.example.com/;
#       }
}
",
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  restart   => '/usr/sbin/service nginx reload',
  require   => Package['nginx'],
}
