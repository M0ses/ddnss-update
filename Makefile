PREFIX=$(DESTDIR)/usr
INSTALL=/usr/bin/install
install:
	[ -d $(PREFIX)/bin ] || mkdir -p $(PREFIX)/bin
	[ -d $(DESTDIR)/etc/ddnss-updater ] || mkdir -p $(DESTDIR)/etc/ddnss-updater
	$(INSTALL) -m 755 bin/ddnss-updater $(PREFIX)/bin/ddnss-updater
