##################################################################
##################################################################
#
GCC=gcc
PATSCC=patscc
PATSOPT=patsopt
#
NIXATS2=nix-shell -p ats2 --run
PATSOPT=\
nix --extra-experimental-features nix-command --extra-experimental-features flakes run github:githwxi/ATS-Postiats\#patsopt --
#
##################################################################
##################################################################
test:: lambda0; ./lambda0
##################################################################
GCFLAG0=-DATS_MEMALLOC_LIBC
GCFLAG1=-DATS_MEMALLOC_GCBDW
##################################################################
lambda0: \
lambda0.dats; \
$(NIXATS2) "patscc $(GCFLAG0) -o $@ $<"
# $(NIXATS2) "patscc $(GCFLAG1) -o $@ $< -lgc"
##################################################################
lambda0_dats: \
lambda0_dats.c ; \
$(PATSCC) -o $@ $(GCFLAG1) $< -lgc
lambda0_dats.c: lambda0.dats; $(PATSOPT) -o $@ -d $<
##################################################################
##################################################################
clean:: ; rm -f *~
clean:: ; rm -f *_dats.c
cleanall:: clean
cleanall:: ; rm -f lambda0
cleanall:: ; rm -f lambda0_dats
##################################################################
####################### end-of-[Makefile] ########################
