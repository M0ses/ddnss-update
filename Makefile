PREFIX=$(DESTDIR)/usr
INSTALL=/usr/bin/install
SYSTEMD_DIR ?= /usr/lib/systemd/system
install:
	[ -d $(PREFIX)/bin ] || mkdir -p $(PREFIX)/bin
	[ -d $(DESTDIR)/etc/cron.d ] || mkdir -p $(DESTDIR)/etc/cron.d
	[ -d $(DESTDIR)/etc/ddnss ] || mkdir -p $(DESTDIR)/etc/ddnss
	$(INSTALL) -m 755 bin/ddnss-update $(PREFIX)/bin/ddnss-update
	[ -f $(DESTDIR)/etc/ddnss/ddnss-update.rc ] || \
		$(INSTALL) -m 644 ./etc/ddnss-update.rc $(DESTDIR)/etc/ddnss/ddnss-update.rc
	$(INSTALL) -m 644 dist/ddnss-update.service $(DESTDIR)$(SYSTEMD_DIR)/ddnss-update.service
	$(INSTALL) -m 644 dist/ddnss-update.timer $(DESTDIR)$(SYSTEMD_DIR)/ddnss-update.timer
