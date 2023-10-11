#!/usr/bin/env puppet
# fix php server issue
exec { 'Web Stack Deubging 3':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell'
