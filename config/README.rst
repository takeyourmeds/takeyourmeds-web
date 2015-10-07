==========
Re-imaging
==========

 * Re-image a new retrosnub machine
 * Create machine with ${name}.takeyourmeds.co.uk
 * After installation:
   - Get IP of server (via `ip addr`) and add/update DNS A record in 123-reg
   - `sed -i -e 's@PermitRootLogin.*@@g' /etc/ssh/sshd_config && service ssh restart`
