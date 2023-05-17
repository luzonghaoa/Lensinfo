import requests
from bs4 import BeautifulSoup
'''
url = "https://fujifilm-x.com/global/products/lenses/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response = requests.get(url, headers=headers)
#print(response)
'''

html_content = """<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <meta content="telephone=no" name="format-detection"/>
  <script src="https://cdn-apac.onetrust.com/consent/c81d9ee0-f5a6-4326-a811-82d129d7e5f0/OtAutoBlock.js" type="text/javascript">
  </script>
  <script charset="UTF-8" data-document-language="true" data-domain-script="c81d9ee0-f5a6-4326-a811-82d129d7e5f0" src="https://cdn-apac.onetrust.com/scripttemplates/otSDKStub.js" type="text/javascript">
  </script>
  <script type="text/javascript">
   function OptanonWrapper() { }
  </script>
  <meta content="article" property="og:type"/>
  <meta content="https://fujifilm-x.com/global/products/lenses/" property="og:url"/>
  <meta content="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/share.png?092000" property="og:image"/>
  <meta content="summary_large_image" name="twitter:card"/>
  <meta content="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/share.png?092000" name="twitter:image"/>
  <meta content="FUJIFILM X Series &amp; GFX – Global" property="og:site_name"/>
  <meta content="FUJIFILM X Series &amp; GFX – Global official site." property="og:description"/>
  <meta content="FUJIFILM X Series &amp; GFX – Global official site." name="description"/>
  <meta content="Lenses | FUJIFILM X Series &amp; GFX – Global" property="og:title"/>
  <link href="https://fujifilm-x.com/wp-content/cache/autoptimize/1/css/autoptimize_d9349d69e4f1eed124f6b3b561a7a5cf.css" media="all" rel="stylesheet"/>
  <title>
   Lenses | FUJIFILM X Series &amp; GFX – Global
  </title>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/favicon.ico" rel="icon" type="image/x-icon"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon.png" rel="apple-touch-icon"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon-57x57.png" rel="apple-touch-icon" sizes="57x57"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon-72x72.png" rel="apple-touch-icon" sizes="72x72"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon-76x76.png" rel="apple-touch-icon" sizes="76x76"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon-114x114.png" rel="apple-touch-icon" sizes="114x114"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon-120x120.png" rel="apple-touch-icon" sizes="120x120"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon-144x144.png" rel="apple-touch-icon" sizes="144x144"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon-152x152.png" rel="apple-touch-icon" sizes="152x152"/>
  <link href="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/apple-touch-icon-180x180.png" rel="apple-touch-icon" sizes="180x180"/>
  <link href="/wp-content/themes/fujifilm-x_jp/assets/css/style.css?20220303" rel="stylesheet"/>
  <link href="/wp-content/themes/fujifilm-x_jp/assets/css/gdpr.css?ver=201910" rel="stylesheet"/>
  <link href="/wp-content/themes/fujifilm-x_jp/assets/css/table_store.css?ver=201910" rel="stylesheet"/>
  <link href="/wp-content/themes/fujifilm-x_jp/assets/css/elementor_custom.css?ver=20210630" rel="stylesheet"/>
  <meta content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" name="robots">
   <link href="https://fujifilm-x.com/global/products/lenses/ja" hreflang="ja-jp" rel="alternate">
    <link href="https://fujifilm-x.com/global/products/lenses/en-au" hreflang="en-au" rel="alternate">
     <link href="https://fujifilm-x.com/global/products/lenses/de-at" hreflang="de-at" rel="alternate">
      <link href="https://fujifilm-x.com/global/products/lenses/nl-be" hreflang="nl-be" rel="alternate">
       <link href="https://fujifilm-x.com/global/products/lenses/fr-be" hreflang="fr-be" rel="alternate">
        <link href="https://fujifilm-x.com/global/products/lenses/en-ca" hreflang="en-ca" rel="alternate">
         <link href="https://fujifilm-x.com/global/products/lenses/fr-ca" hreflang="fr-ca" rel="alternate">
          <link href="https://fujifilm-x.com/global/products/lenses/zh-hans" hreflang="zh-cn" rel="alternate">
           <link href="https://fujifilm-x.com/global/products/lenses/" hreflang="global" rel="alternate">
            <link href="https://fujifilm-x.com/global/products/lenses/el" hreflang="el-gr" rel="alternate">
             <link href="https://fujifilm-x.com/global/products/lenses/it" hreflang="it-it" rel="alternate">
              <link href="https://fujifilm-x.com/global/products/lenses/ko" hreflang="ko-kr" rel="alternate">
               <link href="https://fujifilm-x.com/global/products/lenses/en-us" hreflang="en-us" rel="alternate">
                <link href="https://fujifilm-x.com/global/products/lenses/en-gb" hreflang="en-gb" rel="alternate">
                 <link href="https://fujifilm-x.com/global/products/lenses/br" hreflang="pt-br" rel="alternate">
                  <link href="https://fujifilm-x.com/global/products/lenses/hr" hreflang="hr-hr" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/cs" hreflang="cs-cz" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/da" hreflang="da-dk" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/sl" hreflang="sl-si" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/es" hreflang="es-es" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/sv" hreflang="sv-se" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/fr-ch" hreflang="fr-ch" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/de-ch" hreflang="de-ch" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/th" hreflang="th-th" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/tr" hreflang="tr-tr" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/uk" hreflang="uk-ua" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/vi" hreflang="vi" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/de" hreflang="de-de" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/et" hreflang="et-ee" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/fi" hreflang="fi-fi" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/fr" hreflang="fr-fr" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/hu" hreflang="hu-hu" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/is" hreflang="is-is" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/en-in" hreflang="en-in" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/id" hreflang="id-id" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/ga" hreflang="en-ie" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/lv" hreflang="lv-lv" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/lt" hreflang="lt-lt" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/ms" hreflang="ms" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/nl-nl" hreflang="nl-nl" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/no" hreflang="no-no" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/ph" hreflang="en-ph" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/pl" hreflang="pl-pl" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/pt-pt" hreflang="pt-pt" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/ro" hreflang="ro" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/ru" hreflang="ru-ru" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/en-sg" hreflang="en-sg" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/sk" hreflang="sk-sk" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/en-nz" hreflang="en-nz" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/" hreflang="x-default" rel="alternate"/>
                  <link href="https://fujifilm-x.com/global/products/lenses/zh-hans" rel="canonical"/>
                  <style class="celtispack exc-amp" type="text/css">
                   .widget{margin:0 0 20px 0;}.content-widget-wrapper{padding-top:10px;}.left .Linkunit_async_ads,.left .Responsive_async_ads{float:left;margin-right:16px;margin-left:0;}.right .Linkunit_async_ads,.right .Responsive_async_ads{float:right;margin-right:0;margin-left:16px;}.center .Linkunit_async_ads,.center .Responsive_async_ads{clear:both;text-align:center;margin-right:auto;margin-left:auto;}.widget.Linkunit_async_ads,.widget.Responsive_async_ads,.widget.Smart_async_ads,.widget.Matched_content_ads{background-color:transparent;}.adsense_async_code ins,ins.adsbygoogle{background-color:transparent;}
                  </style>
                  <style class="celtispack exc-amp" type="text/css">
                   .clearfix:after,.clearfix:before{content:' ';display:table;}.clearfix:after{clear:both;zoom:1;}.widget{margin:0 0px 20px 0px;}.content-widget-wrapper{padding-top:10px;}.fit-contain,amp-img.fit-contain img{object-fit:contain;position:relative;width:100%;height:100%;}.fit-cover,amp-img.fit-cover img{object-fit:cover;position:relative;width:100%;height:100%;}.fixed-container{position:relative;width:300px;height:300px;}.cp-post-thumb.fixed-container{float:left;position:relative;width:100px;height:75px;margin:2px 8px 8px 0;}.recent-posts,.related-posts,.popular-ranking{margin:0 8px 8px;padding:0;}.thumb-wrap .rank{font-size:13px;line-height:1.9;text-align:center;color:white;background-color:rgba(4,60,120,0.6);position:relative;top:-70px;left:2px;margin-top:2px;width:24px;height:24px;border-radius:50%;}.post-info{margin:2px 0 0 0;}.post-info .title{line-height:1.2;border:none;word-wrap:break-word;max-height:58px;overflow:hidden;}.post-info .excerpt{font-size:80%;line-height:1.2;padding:5px 0 0;word-wrap:break-word;overflow:hidden;}.post-info .date{font-size:65%;line-height:1;padding:5px 0 0;}.post-info .count{padding:6px 0 0;word-wrap:break-word;}.post-info .count a{font-size:12px;background-color:#FCC;font-weight:bold;font-style:normal;display:inline;color:#F00;padding:0 5px;}.popular-posts-linkurl{float:right;margin:1px 20px 5px 20px;}.prettyprint{padding:8px;font-size:13px;}
                  </style>
                  <style id="global-styles-inline-css" type="text/css">
                   body{--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--duotone--dark-grayscale: url('#wp-duotone-dark-grayscale');--wp--preset--duotone--grayscale: url('#wp-duotone-grayscale');--wp--preset--duotone--purple-yellow: url('#wp-duotone-purple-yellow');--wp--preset--duotone--blue-red: url('#wp-duotone-blue-red');--wp--preset--duotone--midnight: url('#wp-duotone-midnight');--wp--preset--duotone--magenta-yellow: url('#wp-duotone-magenta-yellow');--wp--preset--duotone--purple-green: url('#wp-duotone-purple-green');--wp--preset--duotone--blue-orange: url('#wp-duotone-blue-orange');--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;}:where(.is-layout-flex){gap: 0.5em;}body .is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}body .is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}body .is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}body .is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}body .is-layout-flex{flex-wrap: wrap;align-items: center;}body .is-layout-flex > *{margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
.wp-block-navigation a:where(:not(.wp-element-button)){color: inherit;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}
.wp-block-pullquote{font-size: 1.5em;line-height: 1.6;}
                  </style>
                  <style id="wpml-legacy-dropdown-0-inline-css" type="text/css">
                   .wpml-ls-statics-shortcode_actions, .wpml-ls-statics-shortcode_actions .wpml-ls-sub-menu, .wpml-ls-statics-shortcode_actions a {border-color:#cdcdcd;}.wpml-ls-statics-shortcode_actions a {color:#444444;background-color:#ffffff;}.wpml-ls-statics-shortcode_actions a:hover,.wpml-ls-statics-shortcode_actions a:focus {color:#000000;background-color:#eeeeee;}.wpml-ls-statics-shortcode_actions .wpml-ls-current-language>a {color:#444444;background-color:#ffffff;}.wpml-ls-statics-shortcode_actions .wpml-ls-current-language:hover>a, .wpml-ls-statics-shortcode_actions .wpml-ls-current-language>a:focus {color:#000000;background-color:#eeeeee;}
                  </style>
                  <link href="https://fujifilm-x.com/wp-content/uploads/elementor/css/post-3433221.css" id="elementor-post-3433221-css" media="all" rel="stylesheet" type="text/css"/>
                  <script id="jquery-core-js" src="https://fujifilm-x.com/wp-includes/js/jquery/jquery.min.js" type="text/javascript">
                  </script>
                  <script id="jquery-migrate-js" src="https://fujifilm-x.com/wp-includes/js/jquery/jquery-migrate.min.js" type="text/javascript">
                  </script>
                  <script id="wpml-legacy-dropdown-0-js" src="//fujifilm-x.com/wp-content/plugins/sitepress-multilingual-cms/templates/language-switchers/legacy-dropdown/script.min.js" type="text/javascript">
                  </script>
                  <link href="https://fujifilm-x.com/wp-json/" rel="https://api.w.org/"/>
                  <link href="https://fujifilm-x.com/wp-json/wp/v2/pages/231499" rel="alternate" type="application/json"/>
                  <link href="https://fujifilm-x.com/xmlrpc.php?rsd" rel="EditURI" title="RSD" type="application/rsd+xml"/>
                  <link href="https://fujifilm-x.com/wp-includes/wlwmanifest.xml" rel="wlwmanifest" type="application/wlwmanifest+xml"/>
                  <link href="https://fujifilm-x.com/?p=231499" rel="shortlink"/>
                  <link href="https://fujifilm-x.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ffujifilm-x.com%2Fproducts%2Flenses%2F" rel="alternate" type="application/json+oembed"/>
                  <link href="https://fujifilm-x.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ffujifilm-x.com%2Fproducts%2Flenses%2F&amp;format=xml" rel="alternate" type="text/xml+oembed"/>
                  <meta content="WPML ver:4.6.3 stt:66,67,69,68,82,70,71,59,22,9,12,15,18,4,3,79,13,23,26,78,25,19,27,28,29,31,32,62,73,83,38,80,40,41,44,45,74,10,46,2,50,76,75,52,53,81,54,65,57;" name="generator">
                   <script type="text/javascript">
                    ( function () {
                window.lae_fs = { can_use_premium_code: true};
            } )();
                   </script>
                   <meta content="Elementor 3.13.0; features: a11y_improvements, additional_custom_breakpoints; settings: css_print_method-external, google_font-enabled, font_display-auto" name="generator"/>
                   <style id="wp-custom-css" type="text/css">
                    /** Start Envato Elements CSS: Law Firm (96-3-ffb8a1249063ae6f640b27091bae4b26) **/

/* Kit 93 Custom Styles */
.envato-kit-93-inline-block{
	display: inline-block;
}

.envato-kit-93-drop-cap .elementor-drop-cap-letter{
	margin-top: 18px;
	margin-left: 15px;
}

.envato-kit-93-button .elementor-button{
	width: 100%;
}

/** End Envato Elements CSS: Law Firm (96-3-ffb8a1249063ae6f640b27091bae4b26) **/

.page-template-page-fujifilm-flickr-2023 #intro-section .desktop-only img {
	max-width: 593px !important;
}

.page-template-page-fujifilm-flickr-2023 #x-frame-0 .container > .row > .col .row .repeater > p img {
	max-height: 96px;
	width: auto;
}

.page-template-page-fujifilm-flickr-2023 #x-frame-3 .container > .row .col .row .repeater p img {
	max-height: 96px;
	width: auto;
}
                   </style>
                  </meta>
                 </link>
                </link>
               </link>
              </link>
             </link>
            </link>
           </link>
          </link>
         </link>
        </link>
       </link>
      </link>
     </link>
    </link>
   </link>
  </meta>
 </head>
 <body class="page-template page-template-page-lenses_renew page-template-page-lenses_renew-php page page-id-231499 page-child parent-pageid-231492 elementor-default elementor-kit-3433221 elementor-page elementor-page-231499" id="">
  <noscript>
   <iframe height="0" src="//www.googletagmanager.com/ns.html?id=GTM-NWPVDB" style="display:none;visibility:hidden" width="0">
   </iframe>
  </noscript>
  <script>
   (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
      new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
      j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
      '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
      })(window,document,'script','dataLayer','GTM-NWPVDB');
  </script>
  <div id="wrap">
   <header class="header" id="header">
    <div class="inner">
     <div class="headerlogo">
      <a href="/global/">
       <img alt="X FUJIFILM" src="/wp-content/themes/fujifilm-x_jp/assets/img/common/logo_w.png"/>
      </a>
     </div>
     <div class="subnav">
      <div class="select_country">
       <img alt="A national flag" src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/global.svg"/>
       <p>
        COUNTRY / REGION
       </p>
      </div>
     </div>
     <nav class="globalnav">
      <div class="globalnav__inner">
       <ul>
        <li>
         <a class="toggle" href="/global/products/cameras/">
          PRODUCTS
         </a>
         <div class="globalnav__lowerpage mega">
          <div class="mega_col_wrapper half">
           <p>
            Products by System
           </p>
           <a class="toggle" href="/global/products/cameras/">
           </a>
           <ul class="menu">
            <a class="toggle" href="/global/products/cameras/">
            </a>
            <li>
             <a class="toggle" href="/global/products/cameras/">
             </a>
             <a class="mega_col_heading" href="/global/products/gfx-series/">
              GFX Series
             </a>
            </li>
            <li>
             <a href="/global/products/gfx-series/#cameras">
              Cameras
             </a>
            </li>
            <li>
             <a href="/global/products/gfx-series/#lenses">
              Lenses
             </a>
            </li>
           </ul>
           <ul class="menu">
            <a class="toggle" href="/global/products/cameras/">
            </a>
            <li>
             <a class="toggle" href="/global/products/cameras/">
             </a>
             <a class="mega_col_heading" href="/global/products/x-series/">
              X Series
             </a>
            </li>
            <li>
             <a href="/global/products/x-series/#cameras">
              Cameras
             </a>
            </li>
            <li>
             <a href="/global/products/x-series/#lenses">
              Lenses
             </a>
            </li>
           </ul>
          </div>
          <div class="mega_col_wrapper">
           <p>
            Browse
           </p>
           <a class="toggle" href="/global/products/">
           </a>
           <ul class="menu">
            <a class="toggle" href="/global/products/">
            </a>
            <li>
             <a class="toggle" href="/global/products/cameras/">
             </a>
             <a class="mega_col_heading" href="/global/products/cameras/">
              All Products
             </a>
            </li>
            <li>
             <a href="/global/products/cameras/">
              Cameras
             </a>
            </li>
            <li>
             <a href="/global/products/lenses/">
              Lenses
             </a>
            </li>
            <li>
             <a href="/global/products/accessories/">
              Accessories
             </a>
            </li>
            <li>
             <a href="/global/products/software/">
              Software
             </a>
            </li>
           </ul>
          </div>
          <div class="mega_col_wrapper">
           <div class="clr">
            <p>
             About our products
            </p>
            <a class="toggle" href="/global/global/products/">
            </a>
            <ul class="menu">
             <a class="toggle" href="/global/global/products/">
             </a>
             <li>
              <a class="toggle" href="/global/global/products/">
              </a>
              <a class="mega_col_heading" href="/global/products/x-trans-cmos/">
               Technology
              </a>
             </li>
            </ul>
           </div>
           <div class="clr">
            <p>
             B2B customers
            </p>
            <a class="toggle" href="/global/global/special/">
            </a>
            <ul class="menu">
             <a class="toggle" href="/global/global/special/">
             </a>
             <li>
              <a class="toggle" href="/global/global/special/">
              </a>
              <a class="mega_col_heading" href="/global/special/imaging-solution/">
               Digital Imaging Solutions
              </a>
             </li>
            </ul>
           </div>
          </div>
         </div>
        </li>
        <li>
         <a class="toggle" href="/global/support/">
          SUPPORT
         </a>
         <div class="globalnav__lowerpage">
          <a class="toggle" href="/global/support/">
          </a>
          <ul class="menu" id="menu-header-gnavproduct">
           <a class="toggle" href="/global/support/">
           </a>
           <li>
            <a class="toggle" href="/global/support/">
            </a>
            <li>
             <a href="/global/support/download/">
              Download
             </a>
            </li>
            <li>
             <a href="/global/support/manual/cameras/">
              Manual
             </a>
            </li>
            <li>
             <a href="/global/support/compatibility/cameras/">
              Compatibility
             </a>
            </li>
            <li>
             <a href="https://digitalcamera-support-en.fujifilm.com/" target="_blank">
              FAQ
             </a>
            </li>
           </li>
          </ul>
         </div>
        </li>
        <li>
         <a href="/global/news/">
          NEWS
         </a>
        </li>
        <li>
         <a href="/global/events/">
          EVENTS
         </a>
        </li>
        <a href="/global/events/">
        </a>
        <li class="globalnav__line">
         <a class="toggle" href="/global/photographers/">
          X-Photographers
         </a>
         <div class="globalnav__lowerpage">
          <a class="toggle" href="/global/photographers/">
          </a>
          <ul class="menu" id="menu-header-gnavproduct">
           <a class="toggle" href="/global/photographers/">
           </a>
           <a href="/global/photographers/">
            Galleries
           </a>
           <li>
            <a href="/global/photographers/photographer/">
             Photographer
            </a>
           </li>
           <li>
            <a href="/global/photographers/?camera=GFX_50S">
             Camera
            </a>
           </li>
           <li>
            <a href="/global/photographers/?lens=GF23mmF4_R_LM_WR">
             Lens
            </a>
           </li>
          </ul>
         </div>
        </li>
        <li>
         <a class="" href="/global/stories/">
          X Stories
         </a>
        </li>
       </ul>
       <div class="sp-only select_country">
        <img alt="A national flag" src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/global.svg"/>
        <p>
         COUNTRY / REGION
        </p>
       </div>
       <p class="sp-only copy">
        ©FUJIFILM Corporation.
       </p>
      </div>
     </nav>
     <div class="header__countrybox">
      <div class="btn-close">
       <span>
       </span>
       <span>
       </span>
      </div>
      <div class="header__countrybox__inner" data-simplebar="init">
       <h5>
        SELECT YOUR COUNTRY OR REGION
       </h5>
       <ul>
        <li>
         <a class="toggle" href="#">
          AMERICA
         </a>
         <div class="header__countrybox__lowerpage">
          <ul>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/brazil.svg"/>
            <p>
             <a href="/pt-br/products/lenses/">
              brazil
             </a>
            </p>
           </li>
           <li class="multi">
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/canada.svg"/>
            <p>
             canada (
             <a href="/en-ca/products/lenses/">
              English
             </a>
             ,
             <a href="/fr-ca/products/lenses/">
              French
             </a>
             )
            </p>
           </li>
           <li class="multi">
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/usa.svg"/>
            <p>
             <a href="/en-us/products/lenses/">
              USA
             </a>
            </p>
           </li>
          </ul>
         </div>
        </li>
        <li>
         <a class="toggle" href="#">
          ASIA PACIFIC
         </a>
         <div class="header__countrybox__lowerpage">
          <ul>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/china.svg"/>
            <p>
             <a href="/zh-cn/products/lenses/">
              china
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/india.svg"/>
            <p>
             <a href="/en-in/products/lenses/">
              india
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/indonesia.svg"/>
            <p>
             <a href="/id-id/products/lenses/">
              indonesia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/japan.svg"/>
            <p>
             <a href="/ja-jp/products/lenses/">
              Japan
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/korea.svg"/>
            <p>
             <a href="/ko-kr/products/lenses/">
              korea
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/malaysia.svg"/>
            <p>
             <a href="/en-my/products/lenses/">
              malaysia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/philippines.svg"/>
            <p>
             <a href="/en-ph/products/lenses/">
              Philippines
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/singapore.svg"/>
            <p>
             <a href="/en-sg/products/lenses/">
              singapore
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/thailand.svg"/>
            <p>
             <a href="/th-th/products/lenses/">
              thailand
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/vietnam.svg"/>
            <p>
             <a href="/vi-vn/products/lenses/">
              Vietnam
             </a>
            </p>
           </li>
          </ul>
         </div>
        </li>
        <li>
         <a class="toggle" href="#">
          EUROPE
         </a>
         <div class="header__countrybox__lowerpage">
          <ul>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/austria.svg"/>
            <p>
             <a href="/de-at/products/lenses/">
              austria
             </a>
            </p>
           </li>
           <li class="multi">
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/belgium.svg"/>
            <p>
             belgium (
             <a href="/fr-be/products/lenses/">
              French
             </a>
             ,
             <a href="/nl-be/products/lenses/">
              Dutch
             </a>
             )
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/croatia.svg"/>
            <p>
             <a href="/hr-hr/products/lenses/">
              croatia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/czechia.svg"/>
            <p>
             <a href="/cs-cz/products/lenses/">
              czechia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/denmark.svg"/>
            <p>
             <a href="/da-dk/products/lenses/">
              denmark
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/estonia.svg"/>
            <p>
             <a href="/et-ee/products/lenses/">
              estonia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/finland.svg"/>
            <p>
             <a href="/fi-fi/products/lenses/">
              finland
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/france.svg"/>
            <p>
             <a href="/fr-fr/products/lenses/">
              france
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/germany.svg"/>
            <p>
             <a href="/de-de/products/lenses/">
              germany
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/greece.svg"/>
            <p>
             <a href="/el-gr/products/lenses/">
              greece
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/hungary.svg"/>
            <p>
             <a href="/hu-hu/products/lenses/">
              hungary
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/iceland.svg"/>
            <p>
             <a href="/is-is/products/lenses/">
              iceland
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/ireland.svg"/>
            <p>
             <a href="/en-ie/products/lenses/">
              ireland
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/italy.svg"/>
            <p>
             <a href="/it-it/products/lenses/">
              italy
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/latvia.svg"/>
            <p>
             <a href="/lv-lv/products/lenses/">
              latvia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/lithuania.svg"/>
            <p>
             <a href="/lt-lt/products/lenses/">
              lithuania
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/netherlands.svg"/>
            <p>
             <a href="/nl-nl/products/lenses/">
              netherlands
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/norway.svg"/>
            <p>
             <a href="/no-no/products/lenses/">
              norway
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/poland.svg"/>
            <p>
             <a href="/pl-pl/products/lenses/">
              poland
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/portugal.svg"/>
            <p>
             <a href="/pt-pt/products/lenses/">
              portugal
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/romania.svg"/>
            <p>
             <a href="/ro-ro/products/lenses/">
              romania
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/russia.svg"/>
            <p>
             <a href="/ru-ru/products/lenses/">
              russia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/slovakia.svg"/>
            <p>
             <a href="/sk-sk/products/lenses/">
              slovakia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/slovenia.svg"/>
            <p>
             <a href="/sl-si/products/lenses/">
              slovenia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/spain.svg"/>
            <p>
             <a href="/es-es/products/lenses/">
              spain
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/sweden.svg"/>
            <p>
             <a href="/sv-se/products/lenses/">
              sweden
             </a>
            </p>
           </li>
           <li class="multi">
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/switzerland.svg"/>
            <p>
             switzerland (
             <a href="/de-ch/products/lenses/">
              German
             </a>
             ,
             <a href="/fr-ch/products/lenses/">
              French
             </a>
             )
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/turkey.svg"/>
            <p>
             <a href="/tr-tr/products/lenses/">
              turkey
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/uk.svg"/>
            <p>
             <a href="/en-gb/products/lenses/">
              UK
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/ukraine.svg"/>
            <p>
             <a href="/uk-ua/products/lenses/">
              ukraine
             </a>
            </p>
           </li>
          </ul>
         </div>
        </li>
        <li>
         <a class="toggle" href="#">
          OCEANIA
         </a>
         <div class="header__countrybox__lowerpage">
          <ul>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/australia.svg"/>
            <p>
             <a href="/en-au/products/lenses/">
              australia
             </a>
            </p>
           </li>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/new zealand.svg"/>
            <p>
             <a href="/en-nz/products/lenses/">
              New Zealand
             </a>
            </p>
           </li>
          </ul>
         </div>
        </li>
        <li>
         <a class="toggle" href="#">
          OTHER
         </a>
         <div class="header__countrybox__lowerpage">
          <ul>
           <li>
            <img src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/flag/global.svg"/>
            <p>
             <a href="/global/products/lenses/">
              global
             </a>
            </p>
           </li>
          </ul>
         </div>
        </li>
       </ul>
      </div>
     </div>
     <div class="btn-menu">
      <span>
      </span>
      <span>
      </span>
      <span>
      </span>
     </div>
    </div>
   </header>
   <p>
   </p>
   <main class="">
    <main>
     <section class="products__first lower__first">
      <div class="inner">
       <h1 class="headline_underline">
        Lenses
       </h1>
       <div class="tagline">
        <p>
         The vision of the X Series, the choice for X Series owners.
         <br/>
         A collection of creativity-oriented lenses, which complement the X-Trans CMOS sensor perfectly and eliminate the low-pass filter for ultimate sharpness.
        </p>
       </div>
       <div class="category_tab pdct">
        <input id="css-ac" name="css-ac" type="checkbox"/>
        <label class="sp-only" for="css-ac">
         Select Category
        </label>
        <ul class="products_lnav-menu">
         <li>
          <a href="#model_g-mount">
           G Mount
          </a>
         </li>
         <li>
          <a href="#model_x-mount">
           X Mount
          </a>
         </li>
        </ul>
       </div>
      </div>
     </section>
     <section class="banner_area">
      <ul>
      </ul>
     </section>
     <section class="products__series" id="model_g-mount">
      <div class="inner">
       <h2 class="headline_h2">
        G Mount
       </h2>
       <ul class="category_tab pdct products__series_link products_lnav-menu">
        <li>
         <a href="#g-mount-prime">
          Prime
         </a>
        </li>
        <li>
         <a href="#g-mount-zoom">
          Zoom
         </a>
        </li>
        <li>
         <a href="#g-mount-teleconverter">
          Teleconverter
         </a>
        </li>
       </ul>
       <h3 class="headline_h3" id="g-mount-prime">
        Prime
       </h3>
       <ul class="products__series_list">
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf23mmf4-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2017/04/1_thum_gf23mmf4-r-lm-wr.jpg"/>
          <h3>
           GF23mmF4 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf30mmf35-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2020/06/thum-dgaa.jpg"/>
          <h3>
           GF30mmF3.5 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf45mmf28-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2017/09/2_thum_gf45mmf2-8-r-wr.jpg"/>
          <h3>
           GF45mmF2.8 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf50mmf35-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2019/07/gf50mmf35-R-lm-wr_thum.jpg"/>
          <h3>
           GF50mmF3.5 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf63mmf28-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2017/04/3_thum_gf63mmf2-8-r-wr.jpg"/>
          <h3>
           GF63mmF2.8 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf80mmf17-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2021/01/thum_gf80mmf14-wr-lboe.jpg"/>
          <h3>
           GF80mmF1.7 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf110mmf2-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2017/04/4_thum_gf110mmf2-r-lm-wr.jpg"/>
          <h3>
           GF110mmF2 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf120mmf4-r-lm-ois-wr-macro/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2017/04/5_thum_gf120mmf4-macro-r-lm-ois-wr.jpg"/>
          <h3>
           GF120mmF4 R LM OIS WR Macro
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf250mmf4-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2018/04/6_thum_gf250mmf4-r-lm-ois-wr.jpg"/>
          <h3>
           GF250mmF4 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
       </ul>
       <h3 class="headline_h3" id="g-mount-zoom">
        Zoom
       </h3>
       <ul class="products__series_list">
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf20-35mmf4-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2022/09/1_thum_gf20-35mmf4-r-wr_sdfg.jpg"/>
          <h3>
           GF20-35mmF4 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf32-64mmf4-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2018/06/1_thum_gf32-64mmf4-r-lm-wr-1.jpg"/>
          <h3>
           GF32-64mmF4 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf35-70mmf45-56-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2021/09/1_thum_gf35-70mmf45-56-wr_ghnm-2.jpg"/>
          <h3>
           GF35-70mmF4.5-5.6 WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf45-100mmf4-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2020/01/GF45-100mm-thum.jpg"/>
          <h3>
           GF45-100mmF4 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf100-200mmf56-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2019/01/gf100-200mmf56-r-lm-ois-wr_0117.jpg"/>
          <h3>
           GF100-200mmF5.6 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
       </ul>
       <h3 class="headline_h3" id="g-mount-teleconverter">
        Teleconverter
       </h3>
       <ul class="products__series_list">
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/gf14x-tc-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2018/04/1_thum_gf1-4xtc-wr.jpg"/>
          <h3>
           GF1.4X TC WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
       </ul>
      </div>
     </section>
     <section class="products__series" id="model_x-mount">
      <div class="inner">
       <h2 class="headline_h2">
        X Mount
       </h2>
       <ul class="category_tab pdct products__series_link products_lnav-menu">
        <li>
         <a href="#x-mount-prime">
          Prime
         </a>
        </li>
        <li>
         <a href="#x-mount-zoom">
          Zoom
         </a>
        </li>
        <li>
         <a href="#x-mount-teleconverter">
          Teleconverter
         </a>
        </li>
        <li>
         <a href="#x-mount-cine">
          Cine
         </a>
        </li>
       </ul>
       <h3 class="headline_h3" id="x-mount-prime">
        Prime
       </h3>
       <ul class="products__series_list">
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf14mmf28-r/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/1_thum_xf14mmf2-8-r.jpg"/>
          <h3>
           XF14mmF2.8 R
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf16mmf14-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/2_thum_xf16mmf1-4-r-wr.jpg"/>
          <h3>
           XF16mmF1.4 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf16mmf28-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2019/02/XF16mmF2.8_480x480.jpg"/>
          <h3>
           XF16mmF2.8 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf18mmf14-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2021/04/thum_xf18mmf1.4_haoi.jpg"/>
          <h3>
           XF18mmF1.4 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf18mmf2-r/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/3_thum_xf18mmf2-r.jpg"/>
          <h3>
           XF18mmF2 R
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf23mmf14-r/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/02/4_thum_xf23mmf1-4-r.jpg"/>
          <h3>
           XF23mmF1.4 R
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf23mmf14-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2021/09/1_thum_xf23mmf14_1214-1.jpg"/>
          <h3>
           XF23mmF1.4 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf23mmf2-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2017/04/5_thum_xf23mmf2-r-wr.jpg"/>
          <h3>
           XF23mmF2 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf27mmf28-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2021/01/thum_xf27mmf28-r-wr-lboe.jpg"/>
          <h3>
           XF27mmF2.8 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf30mmf28-r-lm-wr-macro/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2022/10/1_thum_xf30mmf28-r-lm-wr-macro_zxcv.jpg"/>
          <h3>
           XF30mmF2.8 R LM WR Macro
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf33mmf14-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2021/09/1_thum_xf33mmf14-r-lm-wr_nakp-1.jpg"/>
          <h3>
           XF33mmF1.4 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf35mmf14-r/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/7_thum_xf35mmf1-4-r.jpg"/>
          <h3>
           XF35mmF1.4 R
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf35mmf2-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/8_thum_xf35mmf2-r-wr.jpg"/>
          <h3>
           XF35mmF2 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf50mmf1-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2020/09/xf50mmf1-r-wr_feature-ahaf.jpg"/>
          <h3>
           XF50mmF1.0 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf50mmf2-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2017/04/9_thum_xf50mmf2-r-wr.jpg"/>
          <h3>
           XF50mmF2 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf56mmf12-r-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2022/09/1_thum_xf56mmf12-r-wr_qwer.jpg"/>
          <h3>
           XF56mmF1.2 R WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf56mmf12-r-apd/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/11_thum_xfmm56f1-2-r-apd.jpg"/>
          <h3>
           XF56mmF1.2 R APD
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf60mmf24-r-macro/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/12_thum_xf60mmf2-4-r-macro.jpg"/>
          <h3>
           XF60mmF2.4 R Macro
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf80mmf28-r-lm-ois-wr-macro/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2017/09/13_thum_xf80mmf2-8macro.jpg"/>
          <h3>
           XF80mmF2.8 R LM OIS WR Macro
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf90mmf2-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/14_thum_xf90mmf2-r-lm-wr.jpg"/>
          <h3>
           XF90mmF2 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf200mmf2-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2018/07/15_thum_xf200mmf2-r-lm-ois-wr_.jpg"/>
          <h3>
           XF200mmF2 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xc35mmf2/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2020/01/xc35mmf2_thum.jpg"/>
          <h3>
           XC35mmF2
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
       </ul>
       <h3 class="headline_h3" id="x-mount-zoom">
        Zoom
       </h3>
       <ul class="products__series_list">
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf8-16mmf28-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2018/07/1_thum_xf8-16mmf2_8-r-lm-wr.jpg"/>
          <h3>
           XF8-16mmF2.8 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf10-24mmf4-r-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2020/10/xf10-24mmf4-r-ois-wr-product-list.jpg"/>
          <h3>
           XF10-24mmF4 R OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf16-55mmf28-r-lm-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/2_thum_xf16-55mmf2-8-r-lm-wr.jpg"/>
          <h3>
           XF16-55mmF2.8 R LM WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf16-80mmf4-r-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2019/10/xf16-80mmf4-r-ois-wr_thum.jpg"/>
          <h3>
           XF16-80mmF4 R OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf18-55mmf28-4-r-lm-ois/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/5_thum_xf18-55mmf2-8-4-r-lm-ois.jpg"/>
          <h3>
           XF18-55mmF2.8-4 R LM OIS
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf18-120mmf4-lm-pz-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2022/05/1_thum_xf18-120mmf4-lm-pz-wr_fgrt.jpg"/>
          <h3>
           XF18-120mmF4 LM PZ WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf18-135mmf35-56-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/7_thum_xf18-135mmf3-5-5-6-r-lm-ois-wr.jpg.jpg"/>
          <h3>
           XF18-135mmF3.5-5.6 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf50-140mmf28-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/3_thum_xf50-140mmf2_8-r-lm-ois-wr.jpg"/>
          <h3>
           XF50-140mmF2.8 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf55-200mmf35-48-r-lm-ois/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/8_thum_xf55-200mmf3-5-4-8-r-lm-ois.jpg"/>
          <h3>
           XF55-200mmF3.5-4.8 R LM OIS
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf70-300mmf4-56-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2021/01/thum_xf70-300mm-lboe.jpg"/>
          <h3>
           XF70-300mmF4-5.6 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf100-400mmf45-56-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/4_thum_xf100-400mmf4-5-5-6-r-lm-ois-wr.jpg"/>
          <h3>
           XF100-400mmF4.5-5.6 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf150-600mmf56-8-r-lm-ois-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2022/05/1_thum_xf150-600mmf56-8-r-lm-ois-wr_mgpf.jpg"/>
          <h3>
           XF150-600mmF5.6-8 R LM OIS WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xc15-45mmf35-56-ois-pz/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2019/10/9_thum_xc15-45mmf3-5-5-6-ois-pz-1.jpg"/>
          <h3>
           XC15-45mmF3.5-5.6 OIS PZ
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xc50-230mmf45-67-ois-2/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/11_thum_xc50-230mmf4-5-6-7-ois.jpg"/>
          <h3>
           XC50-230mmF4.5-6.7 OIS II
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
       </ul>
       <h3 class="headline_h3" id="x-mount-teleconverter">
        Teleconverter
       </h3>
       <ul class="products__series_list">
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf14x-tc-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/1_thum_xf1-4x-tc-wr.jpg"/>
          <h3>
           XF1.4X TC WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/xf2x-tc-wr/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2016/10/2_thum_xf2x-tc-wr.jpg"/>
          <h3>
           XF2X TC WR
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
       </ul>
       <h3 class="headline_h3" id="x-mount-cine">
        Cine
       </h3>
       <ul class="products__series_list">
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/mkx18-55mmt29/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2018/02/1_thum_mkx18-55mmt2-9.jpg"/>
          <h3>
           MKX18-55mmT2.9
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
        <li>
         <a href="https://fujifilm-x.com/global/products/lenses/mkx50-135mmt29/">
          <img src="https://fujifilm-x.com/wp-content/uploads/2018/02/2_thum_mkx50-135mmt2-9.jpg"/>
          <h3>
           MKX50-135mmT2.9
           <span class="new_text">
           </span>
          </h3>
          <p class="products__series_list_text">
           <span>
           </span>
          </p>
         </a>
        </li>
       </ul>
      </div>
     </section>
     <a href="#wrap" id="pagetop">
     </a>
    </main>
   </main>
   <section class="box_related">
    <h2 class="headline_h2">
     PICKUP
    </h2>
    <ul>
     <li>
      <a href="https://fujifilm-x.com/global/special/imaging-solution/" target="_blank">
       <div class="inner-img">
        <img src="https://fujifilm-x.com/wp-content/uploads/2021/05/imaging_B2B_en_bnr.jpeg"/>
       </div>
       <div class="inner-txt">
        <h3>
         FUJIFILM Digital Imaging Solutions
        </h3>
        <p>
         For Business and Commercial Applications
        </p>
       </div>
      </a>
     </li>
     <li>
      <a href="/global/products/x-trans-cmos/" target="_blank">
       <div class="inner-img">
        <img src="https://fujifilm-x.com/wp-content/uploads/2022/03/pickup-x-trans.jpeg"/>
       </div>
       <div class="inner-txt">
        <h3>
         Technology of X-Trans CMOS
        </h3>
        <p>
         Continuous Evolution on Resolution and Color Reproduction
        </p>
       </div>
      </a>
     </li>
     <li>
      <a href="/global/products/brochure/" target="_blank">
       <div class="inner-img">
        <img src="https://fujifilm-x.com/wp-content/uploads/2019/10/Brochure_Library.jpg"/>
       </div>
       <div class="inner-txt">
        <h3>
         Brochure Library
        </h3>
        <p>
         Read more about our products in these downloadable PDF format brochures
        </p>
       </div>
      </a>
     </li>
     <li>
      <a href="/global/products/x-mount-lens-roadmap/" target="_blank">
       <div class="inner-img">
        <img src="https://fujifilm-x.com/wp-content/uploads/2019/10/X_Mount_lens_roadmap.jpg"/>
       </div>
       <div class="inner-txt">
        <h3>
         X Mount Lens Roadmap
        </h3>
        <p>
         The latest development roadmap for interchangeable lenses for the X Series
        </p>
       </div>
      </a>
     </li>
     <li>
      <a href="/global/products/g-mount-lens-roadmap/" target="_blank">
       <div class="inner-img">
        <img src="https://fujifilm-x.com/wp-content/uploads/2019/10/G_Mount_lens_roadmap.jpg"/>
       </div>
       <div class="inner-txt">
        <h3>
         G Mount Lens Roadmap
        </h3>
        <p>
         The latest development roadmap for interchangeable lenses for the GFX Series
        </p>
       </div>
      </a>
     </li>
    </ul>
   </section>
   <div class="231499">
   </div>
   <a href="#wrap" id="pagetop">
   </a>
   <footer class="footer">
    <div class="inner">
     <div class="crumb">
      <div class="crumb__links">
       <a href="https://fujifilm-x.com">
        HOME
       </a>
       <span>
        Lenses
       </span>
      </div>
     </div>
     <div class="footer__category_main_wrap">
      <dl>
       <dt>
        <a href="/global/products/cameras/">
         PRODUCTS
        </a>
       </dt>
       <dd>
        <ul class="menu" id="menu-header-gnavproduct">
         <li>
          <a href="/global/products/cameras/">
           Cameras
          </a>
         </li>
         <li>
          <a href="/global/products/lenses/">
           Lenses
          </a>
         </li>
         <li>
          <a href="/global/products/accessories/">
           Accessories
          </a>
         </li>
         <li>
          <a href="/global/products/software/">
           Software
          </a>
         </li>
        </ul>
       </dd>
      </dl>
      <dl>
       <dt>
        <a href="/global/support/">
         SUPPORT
        </a>
       </dt>
       <dd>
        <ul class="menu" id="menu-header-gnavproduct">
         <li>
          <a href="/global/support/download/">
           Download
          </a>
         </li>
         <li>
          <a href="/global/support/manual/cameras/">
           Manual
          </a>
         </li>
         <li>
          <a href="/global/support/compatibility/cameras/">
           Compatibility
          </a>
         </li>
         <li>
          <a href="https://digitalcamera-support-en.fujifilm.com/" target="_blank">
           FAQ
          </a>
         </li>
        </ul>
       </dd>
      </dl>
      <dl>
       <dt>
        <a href="/global/photographers/">
         X-Photographers
        </a>
       </dt>
       <dd>
        <ul class="menu" id="menu-header-gnavproduct">
         <a href="/global/photographers/">
          Galleries
         </a>
         <li>
          <a href="/global/photographers/photographer/">
           Photographer
          </a>
         </li>
         <li>
          <a href="/global/photographers/?camera=GFX_50S">
           Camera
          </a>
         </li>
         <li>
          <a href="/global/photographers/?lens=GF23mmF4_R_LM_WR">
           Lens
          </a>
         </li>
        </ul>
       </dd>
      </dl>
      <dl>
       <dt>
        <a href="/global/stories/">
         X Stories
        </a>
       </dt>
       <dd>
        <ul class="menu" id="menu-header-gnavproduct">
         <a href="/global/stories/">
          ALL
         </a>
         <li>
          <a href="/global/stories/?category=be-inspired">
           Be Inspired
          </a>
         </li>
         <li>
          <a href="/global/stories/?category=technology">
           Technology
          </a>
         </li>
         <li>
          <a href="/global/stories/?category=tips-category-stories">
           Tips
          </a>
         </li>
         <li>
          <a href="/global/stories/?category=history">
           History
          </a>
         </li>
         <li>
          <a href="/global/stories/?category=event">
           Event
          </a>
         </li>
         <li>
          <a href="/global/stories/?category=product-movie">
           Product Movie
          </a>
         </li>
         <li>
          <a href="/global/stories/?category=shot-on-x">
           Shot on X
          </a>
         </li>
        </ul>
       </dd>
      </dl>
      <div class="footer__category_sub">
       <ul>
        <li>
         <a href="/global/events/">
          EVENTS
         </a>
        </li>
        <li>
         <a href="/global/news/">
          NEWS
         </a>
        </li>
       </ul>
      </div>
      <div class="sns_area">
       <p class="sns_area-ttl">
        FOLLOW US
       </p>
       <div class="sns_area__world">
        <b>
         Global
        </b>
        <ul>
         <li>
          <a class="facebook" href="https://www.facebook.com/Fujifilmxworld/" target="_blank">
          </a>
         </li>
         <li>
          <a class="youtube" href="https://www.youtube.com/channel/UCZvtcRxo82A4-7BQ2T8MOAA" target="_blank">
          </a>
         </li>
        </ul>
       </div>
      </div>
     </div>
    </div>
    <div class="footer__bottom">
     <div class="footer__bottom_links">
      <ul>
       <li>
        <a href="http://www.fujifilm.com/contact/" target="_blank">
         CONTACT
        </a>
       </li>
       <li>
        <a href="http://www.fujifilm.com/privacy_policy/" target="_blank">
         PRIVACY POLICY
        </a>
       </li>
       <li>
        <a href="http://www.fujifilm.com/terms_of_use/" target="_blank">
         TERMS OF USE
        </a>
       </li>
       <li>
        <a class="optanon-toggle-display">
         Cookie Settings
        </a>
       </li>
      </ul>
     </div>
     <div class="footer__bottom_copy">
      <p>
       <a href="http://www.fujifilm.com/" target="_blank">
        <img alt="FUJIFILM" src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/img/common/footer_logo.png"/>
       </a>
       <span>
        ©FUJIFILM Corporation.
       </span>
      </p>
     </div>
    </div>
   </footer>
   <div class="language">
   </div>
  </div>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/sticky_nav.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/jquery-3.5.1.min.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/jquery.imgloader.min.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/TweenMax.min.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/ScrollToPlugin.min.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/fastclick.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/jquery.collagePlus.min.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/jquery.removeWhitespace.min.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/slick.min.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/jquery.fancybox.min.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/simplebar.js">
  </script>
  <script src="https://fujifilm-x.com/wp-content/themes/fujifilm-x_jp/assets/js/jquery.shave.min.js">
  </script>
  <script src="/wp-content/themes/fujifilm-x_jp/assets/js/script.js?ver=202101140933">
  </script>
  <script src="/wp-content/themes/fujifilm-x_jp/assets/js/gdpr.js">
  </script>
  <script src="/wp-content/themes/fujifilm-x_jp/assets/js/crm.js?ver=20191118">
  </script>
  <script src="https://cdn.jsdelivr.net/npm/exif-js">
  </script>
  <script src="/wp-content/themes/fujifilm-x_jp/assets/js/elementor_custom.js?ver=201910">
  </script>
  <script src="/wp-content/themes/fujifilm-x_jp/assets/js/script_products.js">
  </script>
  <script src="/wp-content/themes/fujifilm-x_jp/assets/js/parts__product_view.js">
  </script>
  <script src="/wp-content/themes/fujifilm-x_jp/assets/js/countdown-x-pro3.min.js?ver=2019092009">
  </script>
  <script id="jquery-ui-core-js" src="https://fujifilm-x.com/wp-includes/js/jquery/ui/core.min.js" type="text/javascript">
  </script>
  <script id="jquery-ui-mouse-js" src="https://fujifilm-x.com/wp-includes/js/jquery/ui/mouse.min.js" type="text/javascript">
  </script>
  <script id="jquery-ui-sortable-js" src="https://fujifilm-x.com/wp-includes/js/jquery/ui/sortable.min.js" type="text/javascript">
  </script>
  <script id="amo_js3-js" src="https://fujifilm-x.com/wp-content/plugins/arrange-multisite-order/js/amo.js" type="text/javascript">
  </script>
  <script id="eae-main-js-extra" type="text/javascript">
   var eae = {"ajaxurl":"https:\/\/fujifilm-x.com\/wp-admin\/admin-ajax.php","current_url":"aHR0cHM6Ly9mdWppZmlsbS14LmNvbS9wcm9kdWN0cy9sZW5zZXMvP2NvdW50cnk9Z2xvYmFsJiMwMzg7bGFuZz0v","breakpoints":{"xs":0,"sm":480,"md":768,"lg":1025,"xl":1440,"xxl":1600}};
var eae_editor = {"plugin_url":"https:\/\/fujifilm-x.com\/wp-content\/plugins\/addon-elements-for-elementor-page-builder\/"};
  </script>
  <script id="eae-main-js" src="https://fujifilm-x.com/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/eae.min.js" type="text/javascript">
  </script>
  <script id="font-awesome-4-shim-js" src="https://fujifilm-x.com/wp-content/plugins/elementor/assets/lib/font-awesome/js/v4-shims.min.js" type="text/javascript">
  </script>
  <script id="animated-main-js" src="https://fujifilm-x.com/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/animated-main.min.js" type="text/javascript">
  </script>
  <script id="eae-particles-js" src="https://fujifilm-x.com/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/js/particles.min.js" type="text/javascript">
  </script>
  <script id="wts-magnific-js" src="https://fujifilm-x.com/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/magnific.min.js" type="text/javascript">
  </script>
  <script id="vegas-js" src="https://fujifilm-x.com/wp-content/plugins/addon-elements-for-elementor-page-builder/assets/lib/vegas/vegas.min.js" type="text/javascript">
  </script>
 </body>
</html>
"""
#print(html_content)


soup = BeautifulSoup(html_content, "html.parser")
res = soup.find(id="model_x-mount")

res = res.find_all('ul')
for _ in res:
    l_ = _.find_all('a')
    if len(l_) > 6:
        for p in l_:
            print(p.h3.text.strip().split('\n')[0])




'''
with open('res.html', 'w+') as f:
    f.write(res.prettify())
'''