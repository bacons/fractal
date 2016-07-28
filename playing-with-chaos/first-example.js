window.onload = function() {
  init();

  function init() {
    console.log('ya?');
    chaos = new Chaos();

    document.body.addEventListener(
      'keyup',
      event => {
        switch (event.keyCode) {
          case 32: // space
            draw();
            break;
          case 80: // p
            chaos.popImage();
            break;
          default:
            break;
        }
      }
    );
  }

  function draw() {
    const x = Math.random() * (chaos.width - 100);
    const y = Math.random() * (chaos.height - 100);
    const w = 20 + Math.random() * 100;
    const h = 20 + Math.random() * 100;
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);

    chaos.context.fillStyle = `rgb(${r},${g},${b}`;
    chaos.context.fillRect(x, y, w, h);
  }
}