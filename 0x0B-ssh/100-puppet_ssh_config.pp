# Client configuration file (w/ Puppet)

file { '~/.ssh/config':
  ensure  => file,
  content => "Host *\nPasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
}
