# eot-cdx-analysis
Documentation and scripts for analyzing the 2008 and 2012 End of Term Web Archive CDX files

## Links to dataset
http://webarchive.library.unt.edu/thumbs/eot_cdx/eot2008_surt_index.cdx.gz (6.3GB)
http://webarchive.library.unt.edu/thumbs/eot_cdx/eot2008_surt_index.cdx.gz.md5
http://webarchive.library.unt.edu/thumbs/eot_cdx/eot2012_surt_index.cdx.gz (9.4GB)
http://webarchive.library.unt.edu/thumbs/eot_cdx/eot2012_surt_index.cdx.gz.md5

## Definition of CDX Fields

### Example
```
gov,loc)/jukebox/search/results?count=20&fq[0]=take_vocal_id:farrar,%20geraldine&fq[1]=take_vocal_id:martinelli,%20giovanni&page=1&q=geraldine%20farrar&referrer=/jukebox/ 20121125005312 http://www.loc.gov/jukebox/search/results?count=20&fq%5B0%5D=take_vocal_id%3AFarrar%2C+Geraldine&fq%5B1%5D=take_vocal_id%3AMartinelli%2C+Giovanni&page=1&q=geraldine+farrar&referrer=%2Fjukebox%2F text/html 200 LFN2AKE4D46XEZNOP3OLXG2WAPLEKZKO - - - 533010532 LOC-EOT2012-001-20121125003355718-04184-15895~wbgrp-crawl012.us.archive.org~8443.warc.gz
gov,loc)/jukebox/search/results?count=20&fq[0]=take_vocal_id:farrar,%20geraldine&fq[1]=take_vocal_id:schumann-heink,%20ernestine&page=1&q=geraldine%20farrar&referrer=/jukebox/ 20121125005219 http://www.loc.gov/jukebox/search/results?count=20&fq%5B0%5D=take_vocal_id%3AFarrar%2C+Geraldine&fq%5B1%5D=take_vocal_id%3ASchumann-Heink%2C+Ernestine&page=1&q=geraldine+farrar&referrer=%2Fjukebox%2F text/html 200 EL5OT5NAXGGV6VADBLNP2CBZSZ5MH6OT - - - 531160983 LOC-EOT2012-001-20121125003355718-04184-15895~wbgrp-crawl012.us.archive.org~8443.warc.gz
gov,loc)/jukebox/search/results?count=20&fq[0]=take_vocal_id:farrar,%20geraldine&fq[1]=take_vocal_id:scotti,%20antonio&page=1&q=geraldine%20farrar&referrer=/jukebox/ 20121125005255 http://www.loc.gov/jukebox/search/results?count=20&fq%5B0%5D=take_vocal_id%3AFarrar%2C+Geraldine&fq%5B1%5D=take_vocal_id%3AScotti%2C+Antonio&page=1&q=geraldine+farrar&referrer=%2Fjukebox%2F text/html 200 SEFDA5UNFREPA35QNNLI7DPNU3P4WDCO - - - 804325022 LOC-EOT2012-001-20121125003257404-04183-15895~wbgrp-crawl012.us.archive.org~8443.warc.gz
gov,loc)/jukebox/search/results?count=20&fq[0]=take_vocal_id:farrar,%20geraldine&fq[1]=take_vocal_id:viafora,%20gina&page=1&q=geraldine%20farrar&referrer=/jukebox/ 20121125005309 http://www.loc.gov/jukebox/search/results?count=20&fq%5B0%5D=take_vocal_id%3AFarrar%2C+Geraldine&fq%5B1%5D=take_vocal_id%3AViafora%2C+Gina&page=1&q=geraldine+farrar&referrer=%2Fjukebox%2F text/html 200 EV6N3TMKIVWAHEHF54M2EMWVM5DP7REJ - - - 532966964 LOC-EOT2012-001-20121125003355718-04184-15895~wbgrp-crawl012.us.archive.org~8443.warc.gz
gov,loc)/jukebox/search/results?count=20&fq[0]=take_vocal_id:homer,%20louise&fq[1]=take_composer_name:campana,%20f.%20&page=1&q=geraldine%20farrar&referrer=/jukebox/ 20121125070122 http://www.loc.gov/jukebox/search/results?count=20&fq%5B0%5D=take_vocal_id%3AHomer%2C+Louise&fq%5B1%5D=take_composer_name%3ACampana%2C+F.+&page=1&q=geraldine+farrar&referrer=%2Fjukebox%2F text/html 200 FW2IGVNKIQGBUQILQGZFLXNEHL634OI6 - - - 661008391 LOC-EOT2012-001-20121125064213479-04227-15895~wbgrp-crawl012.us.archive.org~8443.warc.gz

```

The CDX format in these data files is a space delimited file with the following fields

* SURT formatted URI
* Capture Time
* Original URI
* MIME Type
* Response Code
* Content Hash (SHA1)
* Redirect URL
* Meta tags (not populated)
* Compressed length (sometimes populated)
* Offset in WARC file
* WARC File Name


# Known Data Issues

* Compressed Lengths are not consistantly populated in the CDX fields. 
* Lines that consist of CDX N b a m s k r M S V g are header files for the CDX format and can be ignored

