# configuring  server with Puppet

package {'nginx':
  ensure => present,
}

exec {'installation':
  command  => 'sudo apt-get update -y; sudo apt-get install -y nginx',
  provider => shell.
}

exec {'firewall':
  command  => 'sudo ufw allow "nginx http"',
  provider => shell,
}

exec {'Hello':
  command  => 'echo "Hello world!" | sudo tee /var/www/html/index.nginx-debian.html > /dev/null',
  provider => shell,
}

exec {'err404':
  command  => 'Ceci n\'est pas une page" | sudo tee /var/www/html/custom_404.html > /dev/null',
  provider => shell,
}

exec {'configuration':
  command  => 'sudo sed -i \'0,/location \/ {/ s|location / {|error_page 404 /custom_404.html;\n\n\tlocation  ~ ^/redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=zJ6WbK9zFpI;\n|\' /etc/nginx/sites-available/default',
  provider => shell,
}

exec {
  command => 'sudo service nginx restart',
  provider => shell,
}
