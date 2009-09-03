subarch: amd64
version_stamp: 10.0
target: livecd-stage2
rel_type: default
profile: default/linux/amd64/10.0/desktop
snapshot: 20090826
source_subpath: default/livecd-stage1-amd64-10.0

livecd/bootargs: dokeymap
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-elilo-memtest86+-cdtar.tar.bz2
#livecd/fsscript: /var/svnroot/releng/trunk/releases/10.0/scripts/livecd.sh
livecd/fstype: squashfs
livecd/gk_mainargs: --lvm --dmraid --evms --mdadm --makeopts=-j8
livecd/iso: /tmp/catalyst/builds/default/livedvd-amd64-10.0.iso
livecd/type: gentoo-release-livecd
livecd/volid: Gentoo Linux 10.0 amd64 LiveDVD
livecd/xsession: gnome
livecd/xdm: gdm
livecd/rcadd:
        hald|default
        dbus|default  

#livecd/overlay: /var/svnroot/releng/trunk/releases/10.0/overlays/common/overlay/livecd
#livecd/root_overlay: /var/svnroot/releng/trunk/releases/10.0/overlays/common/root_overlay

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config:  /var/svnroot/releng/trunk/releases/10.0/kconfig/amd64/installcd-2.6.28.config
boot/kernel/gentoo/use: atm fbcondecor mng png truetype usb
boot/kernel/gentoo/packages:
        net-dialup/ppp
        net-dialup/pppconfig
        net-dialup/rp-pppoe
        net-dialup/speedtouch-usb
        net-firewall/iptables
        net-wireless/ndiswrapper
        sys-apps/lm_sensors
        net-wireless/acx-firmware
        net-wireless/atmel-firmware
        net-wireless/b43-fwcutter
        net-wireless/bcm43xx-fwcutter
        net-wireless/zd1201-firmware
        net-wireless/zd1211-firmware                                                           
        sys-block/iscsitarget                  
        net-wireless/zd1211-firmware
        sys-block/iscsitarget
        sys-block/open-iscsi
        net-misc/openswan
# failed
#       sys-apps/pcmcia-cs
        sys-fs/sshfs-fuse
        app-laptop/laptop-mode-tools
        media-libs/alsa-lib
        media-sound/alsa-utils
#       net-dialup/fcdsl   
#       net-dialup/fritzcapi
        net-dialup/globespan-adsl
### Compile failure w/ 2.6.24   
#       net-dialup/slmodem 
        net-misc/br2684ctl
### Compile failure
#       net-wireless/acx
        net-wireless/hostap-utils
        net-wireless/kismet
        sys-apps/pcmciautils
        sys-fs/ntfs3g
	media-libs/alsa-oss

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