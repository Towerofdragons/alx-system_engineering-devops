#kill a process called killmenow
exec {'kill_process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin'
}
