# Copyright 1999-2006 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: /var/cvsroot/gentoo/src/releng/overlays/portage/sys-kernel/vanilla-sources/vanilla-sources-2.4.32.ebuild,v 1.1 2006-09-20 14:23:54 wolf31o2 Exp $

K_NOUSENAME="yes"
K_NOSETEXTRAVERSION="yes"
ETYPE="sources"
inherit kernel-2
detect_version

HOMEPAGE="http://www.kernel.org"
SRC_URI="${KERNEL_URI}"
KEYWORDS="alpha ~ppc sparc x86"