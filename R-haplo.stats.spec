#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-haplo.stats
Version  : 1.8.6
Release  : 23
URL      : https://cran.r-project.org/src/contrib/haplo.stats_1.8.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/haplo.stats_1.8.6.tar.gz
Summary  : Statistical Analysis of Haplotypes with Traits and Covariates
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-haplo.stats-lib = %{version}-%{release}
Requires: R-arsenal
Requires: R-rms
BuildRequires : R-arsenal
BuildRequires : R-rms
BuildRequires : buildreq-R

%description
# haplo.stats
Routines for the analysis of indirectly measured haplotypes. The statistical
methods assume that all subjects are unrelated and that haplotypes are ambiguous
(due to unknown linkage phase of the genetic markers).

%package lib
Summary: lib components for the R-haplo.stats package.
Group: Libraries

%description lib
lib components for the R-haplo.stats package.


%prep
%setup -q -c -n haplo.stats
cd %{_builddir}/haplo.stats

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603386727

%install
export SOURCE_DATE_EPOCH=1603386727
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library haplo.stats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library haplo.stats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library haplo.stats
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc haplo.stats || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/haplo.stats/DESCRIPTION
/usr/lib64/R/library/haplo.stats/INDEX
/usr/lib64/R/library/haplo.stats/Meta/Rd.rds
/usr/lib64/R/library/haplo.stats/Meta/data.rds
/usr/lib64/R/library/haplo.stats/Meta/features.rds
/usr/lib64/R/library/haplo.stats/Meta/hsearch.rds
/usr/lib64/R/library/haplo.stats/Meta/links.rds
/usr/lib64/R/library/haplo.stats/Meta/nsInfo.rds
/usr/lib64/R/library/haplo.stats/Meta/package.rds
/usr/lib64/R/library/haplo.stats/Meta/vignette.rds
/usr/lib64/R/library/haplo.stats/NAMESPACE
/usr/lib64/R/library/haplo.stats/NEWS.Rd
/usr/lib64/R/library/haplo.stats/R/haplo.stats
/usr/lib64/R/library/haplo.stats/R/haplo.stats.rdb
/usr/lib64/R/library/haplo.stats/R/haplo.stats.rdx
/usr/lib64/R/library/haplo.stats/data/hapPower.demo.tab.gz
/usr/lib64/R/library/haplo.stats/data/hla.demo.tab.gz
/usr/lib64/R/library/haplo.stats/data/seqhap.dat.tab.gz
/usr/lib64/R/library/haplo.stats/data/seqhap.pos.tab.gz
/usr/lib64/R/library/haplo.stats/doc/GPL.txt
/usr/lib64/R/library/haplo.stats/doc/LICENSE.mayo
/usr/lib64/R/library/haplo.stats/doc/haplostats.Rnw
/usr/lib64/R/library/haplo.stats/doc/haplostats.pdf
/usr/lib64/R/library/haplo.stats/doc/index.html
/usr/lib64/R/library/haplo.stats/doc/manualHaploStats.pdf.asis
/usr/lib64/R/library/haplo.stats/doc/manualHaploStats.rnwsave
/usr/lib64/R/library/haplo.stats/help/AnIndex
/usr/lib64/R/library/haplo.stats/help/aliases.rds
/usr/lib64/R/library/haplo.stats/help/haplo.stats.rdb
/usr/lib64/R/library/haplo.stats/help/haplo.stats.rdx
/usr/lib64/R/library/haplo.stats/help/paths.rds
/usr/lib64/R/library/haplo.stats/html/00Index.html
/usr/lib64/R/library/haplo.stats/html/R.css
/usr/lib64/R/library/haplo.stats/tests/expanded/dump.varx.s
/usr/lib64/R/library/haplo.stats/tests/expanded/snap.sim.phased.dat
/usr/lib64/R/library/haplo.stats/tests/expanded/snapData.csv
/usr/lib64/R/library/haplo.stats/tests/expanded/snapFUN.s
/usr/lib64/R/library/haplo.stats/tests/expanded/test.Ginv.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.Ginv.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.anova.haplo.glm.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.anova.haplo.glm.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.cc.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.cc.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.design.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.design.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.em.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.em.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.glm.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.glm.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.power.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.scan.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.scan.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.score.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.score.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.score.slide.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.haplo.score.slide.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.methods.haplo.glm.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.methods.haplo.glm.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.seqhap.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.seqhap.Rout.save
/usr/lib64/R/library/haplo.stats/tests/expanded/test.summaryGeno.R
/usr/lib64/R/library/haplo.stats/tests/expanded/test.summaryGeno.Rout.save
/usr/lib64/R/library/haplo.stats/tests/testthat.R
/usr/lib64/R/library/haplo.stats/tests/testthat/cc.hla.adj.rds
/usr/lib64/R/library/haplo.stats/tests/testthat/cc.test.rds
/usr/lib64/R/library/haplo.stats/tests/testthat/fit.gaus.gender.rds
/usr/lib64/R/library/haplo.stats/tests/testthat/fit.gaus.inter.rds
/usr/lib64/R/library/haplo.stats/tests/testthat/powercc.rds
/usr/lib64/R/library/haplo.stats/tests/testthat/test.haplo.cc.R
/usr/lib64/R/library/haplo.stats/tests/testthat/test.haplo.glm.R
/usr/lib64/R/library/haplo.stats/tests/testthat/test.haplo.power.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/haplo.stats/libs/haplo.stats.so
/usr/lib64/R/library/haplo.stats/libs/haplo.stats.so.avx2
/usr/lib64/R/library/haplo.stats/libs/haplo.stats.so.avx512
