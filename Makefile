PREFIX=$(DESTDIR)/usr
INSTALL=/usr/bin/install
install:
	[ -d $(PREFIX)/bin ] || mkdir -p $(PREFIX)/bin
	[ -d $(DESTDIR)/etc/ddnss-update ] || mkdir -p $(DESTDIR)/etc/ddnss-update
	$(INSTALL) -m 755 bin/ddnss-update $(PREFIX)/bin/ddnss-update
