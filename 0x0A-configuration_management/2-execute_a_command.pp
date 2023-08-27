# kill a process

exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => '/usr/bin/pgrep killmenow',
}

