// Venatus Market v3
(function () {
  document.write('<div id="vmv3-ad-manager" style="display:none"></div>');
  document.getElementById("vmv3-ad-manager").innerHTML =
    '<iframe id="vmv3-frm" src="javascript:\'<html><body></body></html>\'" width="0" height="0" data-mode="scan" data-site-id="5a8460b346e0fb0001fc3bac" data-content-width="1120" data-top-space="495"></iframe>';
  var loaderFrame = document.getElementById("vmv3-frm");
  var loaderFrameWindow = loaderFrame.contentWindow
    ? loaderFrame.contentWindow
    : loaderFrame.contentDocument;
  loaderFrameWindow.document.open();
  loaderFrameWindow.document.write(
    "<scr" +
      'ipt src="//hb.vntsm.com/v3/live/ad-manager.min.js" type="text/javascript" async>' +
      "</scr" +
      "ipt>"
  );
  loaderFrameWindow.document.close();
})();
