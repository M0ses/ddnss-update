PREFIX=$(DESTDIR)/usr
INSTALL=/usr/bin/install
install:
	[ -d $(PREFIX)/bin ] || mkdir -p $(PREFIX)/bin
	[ -d $(DESTDIR)/etc/ddnss ] || mkdir -p $(DESTDIR)/etc/ddnss
	$(INSTALL) -m 755 bin/ddnss-update $(PREFIX)/bin/ddnss-update
	[ -f $(DESTDIR)/etc/ddnss/ddnss-update.rc ] || \
		$(INSTALL) -m 644 ./etc/ddnss-update.rc $(DESTDIR)/etc/ddnss/ddnss-update.rc
