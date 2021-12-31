#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lamW
Version  : 2.1.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/lamW_2.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lamW_2.1.0.tar.gz
Summary  : Lambert-W Function
Group    : Development/Tools
License  : BSD-2-Clause
Requires: R-lamW-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppParallel
BuildRequires : R-Rcpp
BuildRequires : R-RcppParallel
BuildRequires : buildreq-R

%description
<!-- badges: start -->
[![CRAN Status Badge](https://www.r-pkg.org/badges/version/lamW)](https://CRAN.R-project.org/package=lamW)
[![](http://cranlogs.r-pkg.org/badges/last-month/lamW)](https://cran.r-project.org/package=lamW)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2022/badge)](https://bestpractices.coreinfrastructure.org/projects/2022)
[![R-CMD-check](https://github.com/aadler/lamW/workflows/R-CMD-check/badge.svg)](https://github.com/aadler/lamW/actions)
[![Codecov test coverage](https://codecov.io/gh/aadler/lamW/branch/master/graph/badge.svg)](https://codecov.io/gh/aadler/lamW?branch=master)
<!-- badges: end -->

%package lib
Summary: lib components for the R-lamW package.
Group: Libraries

%description lib
lib components for the R-lamW package.


%prep
%setup -q -c -n lamW
cd %{_builddir}/lamW

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640965289

%install
export SOURCE_DATE_EPOCH=1640965289
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lamW
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lamW
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lamW
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc lamW || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lamW/CITATION
/usr/lib64/R/library/lamW/DESCRIPTION
/usr/lib64/R/library/lamW/INDEX
/usr/lib64/R/library/lamW/LICENSE
/usr/lib64/R/library/lamW/Meta/Rd.rds
/usr/lib64/R/library/lamW/Meta/features.rds
/usr/lib64/R/library/lamW/Meta/hsearch.rds
/usr/lib64/R/library/lamW/Meta/links.rds
/usr/lib64/R/library/lamW/Meta/nsInfo.rds
/usr/lib64/R/library/lamW/Meta/package.rds
/usr/lib64/R/library/lamW/NAMESPACE
/usr/lib64/R/library/lamW/News.Rd
/usr/lib64/R/library/lamW/R/lamW
/usr/lib64/R/library/lamW/R/lamW.rdb
/usr/lib64/R/library/lamW/R/lamW.rdx
/usr/lib64/R/library/lamW/help/AnIndex
/usr/lib64/R/library/lamW/help/aliases.rds
/usr/lib64/R/library/lamW/help/lamW.rdb
/usr/lib64/R/library/lamW/help/lamW.rdx
/usr/lib64/R/library/lamW/help/paths.rds
/usr/lib64/R/library/lamW/html/00Index.html
/usr/lib64/R/library/lamW/html/R.css
/usr/lib64/R/library/lamW/include/lamW.h
/usr/lib64/R/library/lamW/include/lamW_RcppExports.h
/usr/lib64/R/library/lamW/tests/testthat.R
/usr/lib64/R/library/lamW/tests/testthat/test-lamW.R
/usr/lib64/R/library/lamW/tests/testthat/test-package.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lamW/libs/lamW.so
/usr/lib64/R/library/lamW/libs/lamW.so.avx2
/usr/lib64/R/library/lamW/libs/lamW.so.avx512
