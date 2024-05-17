var buttons = document.querySelectorAll("button");
buttons.forEach(function (button) {
  button.addEventListener("mouseenter", function () {
    button.style.transform = "scale(1.1)";
    button.style.transition = "transform 0.25s ease";
  });
  button.addEventListener("mouseleave", function () {
    button.style.transform = "scale(1)";
    button.style.transition = "transform 0.25s ease";
  });
});
