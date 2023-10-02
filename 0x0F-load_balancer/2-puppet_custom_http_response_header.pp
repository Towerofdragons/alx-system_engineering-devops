exec {'update':
  provide => shell,
  command => 'sudo apt-get update'
}

exec {'nginx_install':
  provider => 'shell',
  command  => 'sudo apt-get -y install nginx'
  before   => Exec['add_header']
}

exec {'add_header':
  command => 'sudo sed -i "s#location / {#location / {\n\tadd_header X-Served-By $HOSTNAME;#" /etc/nginx/sites-enabled/default',
	
  before  => Exec['nginx_restart']
}

exec{'nginx_restart':
  command => 'sudo service nginx restart'
}
