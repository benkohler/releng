subarch: amd64
version_stamp: 2007.0
target: livecd-stage2
rel_type: default
profile: default-linux/amd64/2007.0/desktop
snapshot: 2007.0
source_subpath: default/livecd-stage1-amd64-installer-2007.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/isolinux-3.09-memtest86+-cdtar.tar.bz2
livecd/iso: /var/tmp/catalyst/builds/default/livedvd-amd64-installer-2007.0.iso
livecd/splash_type: gensplash
livecd/splash_theme: livecd-2007.0
livecd/xdm: gdm
livecd/xsession: gnome
livecd/fsscript: /root/livecd/scripts/2007.0/livecd.sh

livecd/type: gentoo-release-livecd
livecd/users: gentoo
livecd/volid: Gentoo Linux AMD64 LiveDVD

livecd/overlay:
	/root/livecd/overlays/2007.0/common/overlay/livedvd
	/root/livecd/overlays/2007.0/amd64/overlay/livedvd
livecd/root_overlay: /root/livecd/overlays/root-livecd

livecd/bootargs: dokeymap
livecd/gk_mainargs: --makeopts=-j16 --lvm2 --dmraid --evms2 --unionfs-dev

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources

boot/kernel/gentoo/config: /root/livecd/kconfig/2007.0/amd64/livecd-2.6.19.config

boot/kernel/gentoo/use: pcmcia usb oss atm truetype png

boot/kernel/gentoo/packages:
	media-gfx/splashutils
	media-gfx/splash-themes-livecd
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
#	net-dialup/fcdsl
#	net-dialup/fritzcapi
#	net-dialup/globespan-adsl
#	net-dialup/slmodem
#	net-wireless/acx
	net-wireless/hostap-utils
	net-wireless/ipw3945
	net-wireless/madwifi-ng-tools
	net-wireless/rt2500
#	net-wireless/rtl8187
	sys-apps/pcmciautils
	sys-fs/cryptsetup-luks

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
	/etc/splash/gentoo
	/etc/splash/emergence
	/usr/share/genkernel/pkg/amd64/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/amd64/*.bz2
