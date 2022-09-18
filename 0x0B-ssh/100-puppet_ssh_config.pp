# Create the ~/.ssh/config with puppet
file {'~/.ssh/config':
  ensure  => present,
  replace => 'yes',
  path    => '/etc/ssh/ssh_config',
  content => 'Host *
     HostName 3.235.148.57
     User root
     IdentityFile ~/.ssh/school',
  mode    => '0664',
}
