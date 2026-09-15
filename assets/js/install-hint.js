// "Add to Home Screen" hint for iPhone and iPad (partials/install-hint.html).
// iOS never offers to install a web app by itself, so without this almost no
// iPhone reader would find out that the site works offline as an app.
document.addEventListener("DOMContentLoaded", function () {
  const hint = document.getElementById("install-hint");
  if (!hint) return;

  const ua = navigator.userAgent;
  const ios = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  // in-app browsers (Instagram, Facebook, …) cannot add to the Home Screen
  const inApp = /FBAN|FBAV|Instagram|Line\/|LinkedInApp|GSA\//.test(ua);
  const installed = navigator.standalone === true || window.matchMedia("(display-mode: standalone)").matches;
  if (!ios || inApp || installed) return;

  const key = "install-hint-closed";
  const days = 30;
  try {
    const closed = Number(localStorage.getItem(key));
    if (closed && Date.now() - closed < days * 864e5) return;
  } catch (e) {}

  hint.hidden = false;
  hint.querySelector("button").addEventListener("click", function () {
    hint.hidden = true;
    try { localStorage.setItem(key, String(Date.now())); } catch (e) {}
  });
});
