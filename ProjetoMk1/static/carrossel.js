/*const carrossel = document.getElementById("carrossel");

let isDown = false;
let startX;
let scrollLeft;

carrossel.addEventListener("mousedown", (e) => {
  isDown = true;
  carrossel.classList.add("active");
  startX = e.pageX - carrossel.offsetLeft;
  scrollLeft = carrossel.scrollLeft;
});

carrossel.addEventListener("mouseleave", () => {
  isDown = false;
  carrossel.classList.remove("active");
});

carrossel.addEventListener("mouseup", () => {
  isDown = false;
  carrossel.classList.remove("active");
});

carrossel.addEventListener("mousemove", (e) => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - carrossel.offsetLeft;
  const walk = (x - startX) * 2;
  carrossel.scrollLeft = scrollLeft - walk;
});

let touchStartX = 0;
let touchScrollLeft = 0;

carrossel.addEventListener("touchstart", (e) => {
  touchStartX = e.touches[0].pageX;
  touchScrollLeft = carrossel.scrollLeft;
}, { passive: true });

carrossel.addEventListener("touchmove", (e) => {
  const touchX = e.touches[0].pageX;
  const walk = (touchX - touchStartX) * -1;
  carrossel.scrollLeft = touchScrollLeft + walk;
}, { passive: true });

carrossel.addEventListener("wheel", function(evt) {
  evt.preventDefault();
  this.scrollLeft += evt.deltaY;
}, { passive: false });
*/