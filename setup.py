from py2deb import Py2deb
from glob import glob

version = "0.1.1"
p=Py2deb("barriosquare")
p.author="Chris J. Burris"
p.mail="chris@chlitechno.com"
p.description="Maemo application to access foursquare.com api functionality"
p["/opt/barrioSquare"] = ["barriosq.py|barriosq","barrioConfig.py","barrioStyles.py","get-location.py","oauth.py","oauthclient.py","loading.gif","loading2.gif","loading.html","refreshing.gif",]
p["/usr/share/applications/hildon"] = ["barrioSquare.desktop",]
p["/usr/share/icons/hicolor/48x48/apps"] = ["barrioSquare.png",]
p["/usr/share/icons/hicolor/64x64/apps"] = ["barrioSquare64.png",]
p.url = "http://www.chilitechno.com/fster"
p.depends="python2.5, python2.5-qt4-common, python2.5-qt4-core, python2.5-qt4-gui, python2.5-qt4-network, python2.5-qt4-webkit, python-location"
p.license="gpl"
p.arch="all"
p.section="net"
# p.postinstall="gtk-update-icon-cache -f /usr/share/icons/hicolor"
p.generate(version)


