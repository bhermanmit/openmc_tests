% 1-group test script

% keff from openmc
keff = 1.76460;

% reaction rates from tallies.out
totrr = 5.2868;
nscatt = 4.28686;
nfiss = 2.66739;

% calculate keff based on tallies
keff_t = nfiss/(totrr - nscatt);

% calculate delta k/k in pcm
pcm = abs(keff_t - keff)/keff*10^5;