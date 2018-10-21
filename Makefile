PREFIX=$(DESTDIR)/usr
INSTALL=/usr/bin/install
SYSTEMD_DIR ?= /usr/lib/systemd/system
LOG_DIR=/var/log/ddnss
install:
	[ -d $(PREFIX)/bin ] || mkdir -p $(PREFIX)/bin
	[ -d $(DESTDIR)/etc/ddnss ] || mkdir -p $(DESTDIR)/etc/ddnss
	[ -d $(DESTDIR)/$(LOGDIR) ] || mkdir -p $(DESTDIR)/$(LOGDIR)
	$(INSTALL) -m 755 bin/ddnss-update $(PREFIX)/bin/ddnss-update
	[ -f $(DESTDIR)/etc/ddnss/ddnss-update.rc ] || \
		$(INSTALL) -m 644 ./etc/ddnss-update.rc $(DESTDIR)/etc/ddnss/ddnss-update.rc
	[ -d $(DESTDIR)$(SYSTEMD_DIR) ] || mkdir -p $(DESTDIR)$(SYSTEMD_DIR)
	$(INSTALL) -m 644 dist/ddnss-update.service $(DESTDIR)$(SYSTEMD_DIR)/ddnss-update.service
	$(INSTALL) -m 644 dist/ddnss-update.timer $(DESTDIR)$(SYSTEMD_DIR)/ddnss-update.timer
