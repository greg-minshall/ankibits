commands=ankicards  ankidecks  ankiimport  ankinotes  ankisearch  ankitags

orgfile=onetag.org

installloc = ~/usr/bin/bin-scripts

all: ${commands}

install: ${commands}
	@for i in  ${commands}; do \
		cmp -s $$i ${installloc}/$$i || \
			(echo installing $$i && \
				cp -p $$i ${installloc}/$$i); \
	done

checkinstall: ${commands}
	@for i in  ${commands}; do \
		cmp -s $$i ${installloc}/$$i || \
			echo need to install $$i; \
	done

${commands}: ${orgfile}
	./dotangle.el ${orgfile}
