# Define a class for custom HTTP response header
class custom_http_response_header {

  package { 'nginx':
    ensure => 'installed',
  }

  # Create a custom Nginx config file
  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => 'present',
    content => "server {\n    listen 80 default_server;\n    listen [::]:80 default_server;\n\n    root /var/www/html;\n    index index.html;\n\n    location /redirect_me {\n        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n    }\n\n    error_page 404 /404.html;\n    location = /404.html{\n        internal;\n    }\n\n    add_header X-Served-By $::hostname;\n}\n",
    notify  => Service['nginx'],
  }

  # Ensure Nginx is running
  service { 'nginx':
    ensure => 'running',
    enable => true,
  }
}

# Apply the custom HTTP response header class
include custom_http_response_header

