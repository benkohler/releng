subarch: i686
version_stamp: 10.0
target: livecd-stage2
rel_type: default
profile: default/linux/x86/10.0/desktop
snapshot: 20090905
source_subpath: default/livecd-stage1-i686-10.0

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm --makeopts=-j16
livecd/iso: /var/tmp/catalyst/builds/default/livedvd-i686-10.0.iso
livecd/type: gentoo-release-livedvd
livecd/volid: Gentoo Linux 10.0 x86 LiveDVD
livecd/xdm: gdm
livecd/xsession: gnome
livecd/rcadd: 
	hald|default 
	dbus|default

boot/kernel: gentoo

boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /var/svnroot/releng/trunk/releases/10.0/kconfig/x86/installcd-2.6.30.config
boot/kernel/gentoo/use: atm fbcondecor mng png truetype usb
boot/kernel/gentoo/packages:
# keywords.
#	net-wireless/rt73-firmware
        net-dialup/ppp
	net-dialup/pppconfig
        net-dialup/rp-pppoe
        net-dialup/speedtouch-usb
        net-firewall/iptables
        net-wireless/ndiswrapper
        sys-apps/lm_sensors
        net-wireless/acx-firmware
# keywords.
#        net-wireless/atmel-firmware
        net-wireless/b43-fwcutter
# keywords.
#        net-wireless/bcm43xx-fwcutter
        net-wireless/zd1201-firmware
        net-wireless/zd1211-firmware
        sys-block/iscsitarget
# keywords.
#        sys-block/open-iscsi
        net-misc/openswan
# failed
#       sys-apps/pcmcia-cs
        sys-fs/sshfs-fuse
	app-laptop/laptop-mode-tools
	media-libs/alsa-lib
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
	net-dialup/globespan-adsl
### Compile failure w/ 2.6.24
#	net-dialup/slmodem
	net-misc/br2684ctl
### Compile failure
#	net-wireless/acx
	net-wireless/hostap-utils
	net-wireless/kismet
	sys-apps/pcmciautils
	sys-fs/ntfs3g

livecd/unmerge:
	sys-kernel/gentoo-sources
	
livecd/empty:
	/var/tmp
	/var/empty
	/var/run
	/var/state
	/var/cache/edb/dep
	/tmp
	/usr/portage
	/usr/src
	/root/.ccache
	/usr/share/genkernel/pkg/x86/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/x86/*.bz2
