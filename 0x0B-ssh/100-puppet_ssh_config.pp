# Client configuration file (w/ Puppet)

file_line{'Refuse to authenticate using a password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line{'Declare configuration file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}
