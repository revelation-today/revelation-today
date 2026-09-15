document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".sb-btn");
  buttons.forEach(function (button) {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      const list = button.parentElement.parentElement;
      if (list) {
        list.classList.toggle("open")
      }
    });
  });
});
