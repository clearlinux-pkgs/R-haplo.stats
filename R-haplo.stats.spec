#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-haplo.stats
Version  : 1.7.9
Release  : 14
URL      : https://cran.r-project.org/src/contrib/haplo.stats_1.7.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/haplo.stats_1.7.9.tar.gz
Summary  : Statistical Analysis of Haplotypes with Traits and Covariates
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-haplo.stats-lib = %{version}-%{release}
Requires: R-Hmisc
Requires: R-TH.data
Requires: R-acepack
Requires: R-base64enc
Requires: R-gridExtra
Requires: R-htmlTable
Requires: R-latticeExtra
Requires: R-multcomp
Requires: R-munsell
Requires: R-polspline
Requires: R-rms
BuildRequires : R-Hmisc
BuildRequires : R-TH.data
BuildRequires : R-acepack
BuildRequires : R-base64enc
BuildRequires : R-gridExtra
BuildRequires : R-htmlTable
BuildRequires : R-latticeExtra
BuildRequires : R-multcomp
BuildRequires : R-munsell
BuildRequires : R-polspline
BuildRequires : R-rms
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-haplo.stats package.
Group: Libraries

%description lib
lib components for the R-haplo.stats package.


%prep
%setup -q -c -n haplo.stats

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562200573

%install
export SOURCE_DATE_EPOCH=1562200573
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
/usr/lib64/R/library/haplo.stats/LICENSE.note
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
/usr/lib64/R/library/haplo.stats/doc/index.html
/usr/lib64/R/library/haplo.stats/doc/manualHaploStats.pdf
/usr/lib64/R/library/haplo.stats/doc/manualHaploStats.pdf.asis
/usr/lib64/R/library/haplo.stats/help/AnIndex
/usr/lib64/R/library/haplo.stats/help/aliases.rds
/usr/lib64/R/library/haplo.stats/help/haplo.stats.rdb
/usr/lib64/R/library/haplo.stats/help/haplo.stats.rdx
/usr/lib64/R/library/haplo.stats/help/paths.rds
/usr/lib64/R/library/haplo.stats/html/00Index.html
/usr/lib64/R/library/haplo.stats/html/R.css
/usr/lib64/R/library/haplo.stats/tests/dump.varx.s
/usr/lib64/R/library/haplo.stats/tests/snap.sim.phased.dat
/usr/lib64/R/library/haplo.stats/tests/snapData.csv
/usr/lib64/R/library/haplo.stats/tests/snapFUN.s
/usr/lib64/R/library/haplo.stats/tests/test.haplo.cc.R
/usr/lib64/R/library/haplo.stats/tests/test.haplo.cc.Rout.save
/usr/lib64/R/library/haplo.stats/tests/test.haplo.em.R
/usr/lib64/R/library/haplo.stats/tests/test.haplo.em.Rout.save
/usr/lib64/R/library/haplo.stats/tests/test.haplo.power.R
/usr/lib64/R/library/haplo.stats/tests/test.haplo.power.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/haplo.stats/libs/haplo.stats.so
/usr/lib64/R/library/haplo.stats/libs/haplo.stats.so.avx2
/usr/lib64/R/library/haplo.stats/libs/haplo.stats.so.avx512
