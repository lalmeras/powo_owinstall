# override installation settings

# ignore ssl errors
#common:
#  validate_ssl_certs: false

# configure proxy access
#env_vars:
#  PIP_INDEX_URL: http://192.168.124.1:3141/root/pypi
#  PIP_TRUSTED_HOST: 192.168.124.1
#  http_proxy: http://192.168.124.1:3128/
#  https_proxy: http://192.168.124.1:3128/
#  no_proxy: localhost,127.0.0.1,192.168.124.1,github.com

# configure account creation
powo_user: vagrant
powo_home: /home/vagrant
powo_fullname: vagrant

# override rdesktop -n option (needed in case of license issue)
remote:
  client_hostname: vagrant10

# override checksum / download url
# add new distributions
#eclipse:
#    distributions:
#        owsi-4.5-x86_64:
#            url: __CUSTOM_URL__
#            checksum: md5:acef115f0b46bce8750c704f0421759a
#
#jdk:
#    distributions:
#        1.7.71-x86_64:
#            url: __CUSTOM_URL__
#
#maven:
#    distributions:
#        3.2.1:
#            url: __CUSTOM_URL__
#
#tomcat:
#    distributions:
#        7.0.53:
#            url: __CUSTOM_URL__
