==========
Re-imaging
==========

* Re-image a new retrosnub machine with Debian jessie:
  - Call it ${name}.takeyourmeds.co.uk
  - Don't worry about the non-root user.
  - Select all other defaults
* Get IP of server (via `ip addr`)
* `sed -i -e 's@PermitRootLogin.*@@g' /etc/ssh/sshd_config && service ssh restart`
* `mkdir /root/deployhq`
* Add/update DNS A record in 123-reg
* Add "SSH/SCP" server to DeployHQ
  - Use root user and root password configured earlier
  - Set "Deployment path" to `/root/deployhq`
